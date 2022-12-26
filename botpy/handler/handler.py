import logging
import subprocess as sub  # needed for softreload to pull from git kekw
import sys
from datetime import datetime
from importlib import reload
from time import sleep
from typing import Optional

import discord
from discord.errors import Forbidden  # api library
from discord.ext.commands import Bot

from botpy.botlogger import botlogger
from botpy.cmd import commandhandler  # module for commandhandling
from botpy.loops import loophandler as loop
from botpy.msglist import msglist  # module for message tracking
from botpy.sql import dbhandler  # module for all things sqlite
from botpy.uptime import uptime  # module to track uptime of bot

IMPORTS = (botlogger, msglist, dbhandler, commandhandler, uptime, loop)

SUDOID = 291291715598286848

logger = logging.getLogger("botlogger")

ISRELOADING = True
PREFIX = "°"  # default value for initialization


# HACK these globals are super sketchy...

time_tracker: uptime.Uptime
msgs: msglist.Msglist = None  # type: ignore
cmdhandler: commandhandler.CommandHandler = None  # type: ignore
db: dbhandler.Dbhandler = None  # type: ignore


def init(client: Bot, STARTTIME: datetime):
    global cmdhandler, time_tracker, msgs, db, PREFIX
    time_tracker = uptime.Uptime(STARTTIME)
    msgs = msglist.Msglist(5)
    db = dbhandler.Dbhandler("discordbot.db")
    try:
        prefix_in_db = db.get_from_misc("prefix")
        if prefix_in_db:
            PREFIX = prefix_in_db
        else:
            PREFIX = "°"  # fallback :>

        if int(db.get_from_misc("debug")) > 0:
            print("DEBUGGING MODE. PREFIX IS: ", PREFIX)

    except Exception as e:
        print(e)
        PREFIX = "&"

    cmdhandler = commandhandler.CommandHandler(
        dbhandler_instance=db,
        msgs=msgs,
        PREFIX=PREFIX,
        client=client,
        time_tracker=time_tracker,
    )
    botlogger.get_ready()


this_emote = "<:this:747783377662378004>"


def perm_valid(cmd: str, permlevel: int) -> bool:
    return permlevel >= db.get_cmd_perm(cmd)


async def add_reaction(message, emote):
    try:
        await message.add_reaction(emote)
        return 0
    except discord.errors.Forbidden:
        return 5
    except discord.errors.HTTPException as e:
        logger.warning("Couldn't add emote as reaction:" + emote)
        print(e)
        return 1


def get_ready(client: Bot, STARTTIME):
    global msgs, db, time_tracker, cmdhandler, PREFIX
    msgs = msglist.Msglist(5)
    db = dbhandler.Dbhandler("discordbot.db")
    PREFIX = db.get_from_misc("prefix")
    time_tracker = uptime.Uptime(STARTTIME)
    cmdhandler = commandhandler.CommandHandler(
        dbhandler_instance=db,
        msgs=msgs,
        PREFIX=PREFIX,
        client=client,
        time_tracker=time_tracker,
    )
    last_msgs_backup = cmdhandler.last_MSG
    cmdhandler.last_MSG = last_msgs_backup
    botlogger.get_ready()


async def doreload(
    message: discord.Message,
    client: Bot,
    STARTTIME,
    msgs_backup,
):  # reloads all dependencies
    global ISRELOADING

    work_to_do = True
    backoff = 10
    is_recovering = False

    reload(discord)
    await loop.discard(client)
    embed = discord.Embed(title="Soft Reloading")
    while work_to_do:
        failedmodules = ""
        modulenames = "discord.py\nhandler\n"
        submodules = set()
        for module in IMPORTS:
            try:
                reload(module)
            except ModuleNotFoundError as e:
                failedmodules += module.__name__ + "\n"
                failedmodules += "⤷" + str(e).split("'")[1] + "\n"
                continue
            modulenames += module.__name__ + "\n"
            try:
                module.IMPORTS
            except AttributeError:
                logger.error(f"{module.__name__} missing IMPORTS list")
                continue
            for subimport in module.IMPORTS:
                if subimport not in submodules:
                    submodules.add(subimport)
                    modulenames += "⤷" + subimport.__name__ + "\n"
                    for subsub in subimport.IMPORTS:
                        if subsub not in submodules and subsub not in IMPORTS:
                            submodules.add(subsub)
                            modulenames += "➥  " + subsub.__name__ + "\n"

        for submodule in submodules:
            try:
                reload(submodule)
            except ModuleNotFoundError as e:
                failedmodules += "➥" + str(e).split("'")[1] + "\n"
                continue

        embed = discord.Embed(title="Soft Reloading")
        embed.add_field(name="✅ Reloaded modules:", value=modulenames)
        embed.set_author(
            name=message.author.name,
            icon_url=message.author.avatar.url if message.author.avatar else None,
        )
        embed.timestamp = uptime.get_now_utc()

        if is_recovering:  # if already retrying
            await msgs_backup.pop().delete()  # dont clutter

        if (
            len(failedmodules.strip()) > 0
        ):  # this applies when anything failed during reloading
            embed.add_field(name="❌ Couldn't import:", value=failedmodules)
            embed.add_field(
                name="BackOff-Retry", value=f"Will retry loading in {backoff} seconds"
            )

            is_recovering = True

            sent_msg = await message.channel.send(embed=embed)
            msgs_backup.append(
                sent_msg
            )  # keep the message list up to date until it gets put to cmdhandler again

            sleep(backoff)  # wait until next reload
            backoff *= 2  # exponential backoff

            sub.run(
                ["git", "pull", "--no-edit"]
            )  # git pull --no-edit -> get newest changes from github
        else:
            work_to_do = False

    if backoff > 512:  # give up at some point
        logger.fatal(
            "gave up on reloading after trying multiple times.. something really doesnt work here"
        )
        sys.exit(1)  # give up with nonzero error code

    # at this point everything should be fine
    get_ready(client=client, STARTTIME=STARTTIME)
    res = 0
    cmdhandler.last_MSG = msgs_backup
    cmdhandler.curr_msg = message

    logger.info("Return from softreload")
    callee = message.author.name
    if isinstance(message.author, discord.Member) and message.author.nick is not None:
        callee = message.author.nick

    res = max(
        await cmdhandler.sendMsg(
            channel=message.channel,
            toSend=embed,
            caller=callee,
            caller_pic=message.author.avatar.url
            if message.author.avatar is not None
            else None,
        ),
        res,
    )
    await add_reaction(message, db.get_emote(res))
    ISRELOADING = False
    if isinstance(message.channel, discord.TextChannel):
        try:
            await message.delete()
        except Forbidden:
            pass  # cant do anyting :shrug:


async def do_the_thing(message: discord.Message):
    await message.add_reaction("🤫")


async def handle(message: discord.Message) -> Optional[int]:
    global ISRELOADING
    global PREFIX
    if ISRELOADING:
        return 0  # prevent errors during reloading
    # block bots
    if message.author.bot and not message.author.id == cmdhandler.toTrackID:
        return 0

    # count messages per user
    db.increment_user_message_count(
        message.author.id, message.author.name, message.author.mention
    )

    if (
        message.guild
        and message.guild.id in (747752542741725244, 695246759382745108)
        and message.content.startswith("$g")
        and len(args := message.content.split(" ")) > 1
        and args[1].isnumeric()
    ):
        db.add_average(message.author.id, int(args[1]))

    is_command = message.content.startswith(PREFIX)
    permlevel = db.get_perm_level(message.author.id)
    is_joniii = message.author.id == SUDOID  # hardcode that sucker
    if is_joniii:
        permlevel = 10
    cmd = db.find_alias(message.content[1:].split(" ")[0].lower())

    if (
        int(db.get_from_misc("standby")) == 1 and cmd != "deepsleep"
    ):  # ignore everything in standby
        return

    # easteregg lel
    if "177013" in message.content.strip().replace(" ", "") and not is_command:
        await do_the_thing(message)
    if is_command:
        logger.info(f"{message.author.name}>{message.content}")

    if message.author.id == cmdhandler.toTrackID and not is_command:
        msgs.add_msg(message)
        if db.shouldAnnoy():
            await add_reaction(message, this_emote)

    if is_command and cmd:
        # prevent handling invalid commands
        # find_alias returns "" on unknown commands and bool("") is False :>

        if cmd == "" or not perm_valid(
            cmd, permlevel
        ):  # !!! perms already checked heree
            res = 4

        # special case with soft reload that only reloads the modules
        elif cmd == "softreload" and perm_valid(cmd, permlevel):
            ISRELOADING = True
            db.close_down()
            return 88

        else:
            res = await cmdhandler.handle(message, permlevel)
        if res == 99:  # RELOAD
            db.close_down()
            return 99
        elif res == 77:  # update prefix
            PREFIX = db.get_from_misc("prefix")
            res = 0  # set to normal reaction
        await add_reaction(message, db.get_emote(res))
        if isinstance(message.channel, discord.TextChannel):
            await message.delete(delay=3)
