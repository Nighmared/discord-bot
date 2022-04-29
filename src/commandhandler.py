import logging
import traceback
from sqlite3 import OperationalError
from sys import version_info as python_version
from time import time as current_time_sec

import discord
import discord.ext.commands
from discord.channel import TextChannel
from discord.errors import Forbidden, NotFound

import dbhandler
import inspirobot
import issues
import loops.polyring as polyring
import meme
import msglist
import neko
import robohash
import shorten
import stalk
import xkcd
from nhentai import nhentai

IMPORTS = (
    neko,
    issues,
    nhentai,
    inspirobot,
    meme,
    stalk,
    robohash,
    shorten,
    xkcd,
    polyring,
)
logger = logging.getLogger("botlogger")


cmd_handling_funcs = {}


def command(func):
    cmd_handling_funcs[func.__name__] = func
    return func


class CommandHandler:
    ISSUECOLOR = 0x00F0F0  # lightblue
    TRACKERCOLOR = 0x660066  # pinkish
    SYSTEMCOLOR = 0x009900  # green
    QUERYCOLOR = 0xFFCC00  # yellow
    MISCCOLOR = 0xCC6699
    NORMALCOLOR = 0x000000  # black
    ERRORCOLOR = 0xFF0000  # red
    FIELDSIZELIMIT = 1024
    EMBEDSIZELIMIT = 5950
    MAXNUMBEROFEMBEDS = 25
    ALLOWEDSOURCEFILES = {
        "dbhandler": "dbhandler.py",
        "db": "dbhandler.py",
        "issues": "issues.py",
        "msglist": "msglist.py",
        "neko": "neko.py",
        "nhentai": "nhentai/nhentai.py",
        "uptime": "uptime.py",
        "push": "push.sh",
        "runner": "runner.sh",
        "main": "bot.py",
        "bot": "bot.py",
        "commandhandler": "commandhandler.py",
        "cmd": "commandhandler.py",
        "handler": "handler.py",
        "msg": "handler.py",
        "inspire": "inspirobot.py",
        "meme": "meme.py",
        "robohash": "robohash.py",
        "rh": "robohash.py",
        "shorten": "shorten.py",
        "xkcd": "xkcd.py",
        "test": "test_sanity_check.py",
        "loop": "loophandler.py",
        "polyring": "loops/polyring.py",
    }

    def __init__(
        self,
        dbhandler_instance: dbhandler.Dbhandler,
        msgs: msglist,
        PREFIX: str,
        time_tracker,
        client: discord.ext.commands.Bot,
    ):
        self.msgs = msgs
        self.dbhandler = dbhandler_instance
        self.toTrackID = 0
        self.toTrackName = "nobody"
        self.toTrackUser = None
        self.last_MSG = []
        self.PREFIX = PREFIX
        self.client = client
        self.uptime_tracker = time_tracker
        self.nh_handler = nhentai.Handler(self.dbhandler)

    def perm_valid(self, cmd: str, permlevel: int) -> bool:
        return permlevel >= self.dbhandler.get_cmd_perm(cmd)

    async def sendMsg(
        self,
        channel,
        toSend: discord.Embed,
        file=None,
        callee="INVALID",
        callee_pic: str = None,
    ):
        try:
            if type(toSend) == discord.embeds.Embed:
                if callee == "INVALID":
                    toSend.set_footer(
                        text=f"Answering to {self.curr_msg.author.name}\n <fix footer for dis cmd>"
                    )  # tf is this line??? FIXME
                else:
                    toSend.set_author(name=callee, icon_url=callee_pic)
                    toSend.timestamp = (
                        self.uptime_tracker.get_now_utc()
                    )  # important cuz for some reason discord adjusts time assuming utc time...
                if file is not None:
                    self.last_MSG.append(await channel.send(file=file, embed=toSend))
                else:
                    self.last_MSG.append(await channel.send(embed=toSend))
            else:  # only the case for say command
                self.last_MSG.append(await channel.send(str(toSend)))
            return 0
        except discord.Forbidden:
            return 5

    async def handle(self, message: discord.Message, permlevel: int) -> int:
        self.curr_msg = message
        args = message.content[1:].split(" ")
        cmd = args[0].lower()
        cmd = self.dbhandler.find_alias(cmd)
        if cmd == "":
            logger.warning(
                f"{message.author.name}#{message.author.discriminator} tried to use an invalid command"
            )
            return 3
        if not self.dbhandler.cmd_is_enabled(cmd):
            error = 4
            logger.warning(
                f"{message.author.name}#{message.author.discriminator} tried to use a disabled command ({cmd})"
            )
            return error
        error = 0

        if not self.perm_valid(cmd, permlevel):
            return 4

        try:
            callee = (
                message.author.nick
                if message.author.nick is not None
                else message.author.name
            )
        except AttributeError:
            callee = message.author.name

        if cmd == "reload":
            error, embObj = await self.reload(message)
            if (
                await self.sendMsg(
                    channel=message.channel,
                    toSend=embObj,
                    callee=callee,
                    callee_pic=message.author.avatar_url,
                )
                > 0
            ):
                error = 1  # DONT FIX THIS, IS SPECIAL FOR RELOAD
            return error
        # general case
        # res = await self.cmd_handling_funcs[cmd](message)
        res = await cmd_handling_funcs[cmd](self, message)
        if len(res) == 2:
            error, embObj = res
            file = None
        else:
            error, embObj, file = res
        if embObj is not None:

            err2 = await self.sendMsg(
                message.channel,
                embObj,
                callee=callee,
                file=file,
                callee_pic=message.author.avatar_url,
            )
            error = (error, err2)[error == 0]
        return error

    @command
    async def addcommand(self, message: discord.Message) -> tuple:
        try:
            args = message.content[1:].split(" ")
            self.dbhandler._execComm(
                f"""
			INSERT INTO commands(
				"cmdname",
				"permlevel",
				"helptext",
				"alias",
				"enabled"
				)
			VALUES(
				"{args[1]}",
				{args[2]},
				"{args[3]}",
				"{args[4]}",
				"{args[5]}"
				)"""
            )
            return (0, None)
        except (OperationalError, IndexError):
            embObj = discord.Embed(
                title="Addcommand",
                description=f"Usage: {self.PREFIX}addcommand <cmdname:str> <permlevel:int> <help_text:str> <alias:str> <enabled:[0,1]>",
                color=self.QUERYCOLOR,
            )
            return (3, embObj)

    @command
    async def add_meme_template(self, message: discord.Message) -> tuple:
        try:
            args = message.content[1:].split(" ")
            template_name = args[1]
            template_id = args[2].strip()
            self.dbhandler.add_meme_template(template_name, int(template_id))
            return (0, None)
        except Exception:
            return (1, None)

    @command
    async def banner(self, message: discord.Message) -> tuple:
        try:
            channel, guild = message.channel, message.guild
            banner_url = guild.banner_url
            embObj = discord.Embed(
                title="Banner", description=guild.name, color=self.NORMALCOLOR
            )
            embObj.set_image(url=banner_url)
            return (0, embObj)
        except:
            return (1, None)

    @command
    async def changelog(self, message: discord.Message) -> tuple:
        try:
            embObj = discord.Embed(
                title="Latest Changes",
                description=self.dbhandler.get_from_misc("changelog"),
                color=self.SYSTEMCOLOR,
            )
            return (0, embObj)
        except OperationalError:
            embObj = discord.Embed(
                title="Latest Changes",
                description="-- Something went wrong with DB --",
                color=self.SYSTEMCOLOR,
            )
            return (1, embObj)

    @command
    async def createbackup(self, message: discord.Message) -> tuple:
        error = self.dbhandler.create_backup()
        res = ("Created Backup of DB", "Something went wrong")[error > 0]
        embObj = discord.Embed(title="Backup", description=res, color=self.QUERYCOLOR)
        return (error, embObj)

    @command
    async def deepsleep(self, message: discord.Message) -> tuple:
        try:
            self.dbhandler.set_to_misc(
                "standby", (1, 0)[int(self.dbhandler.get_from_misc("standby"))]
            )
            embObj = discord.Embed(
                title="DeepSleep Mode",
                description=f"{('leaving','entering')[int(self.dbhandler.get_from_misc('standby'))]} ~~Lockdown~~ DeepSleep mode",
                color=self.SYSTEMCOLOR,
            )
            return (0, embObj)
        except OperationalError:
            embObj = discord.Embed(
                title="DeepSleep Mode",
                description="-- Something went wrong with DB --",
                color=self.SYSTEMCOLOR,
            )
            return (1, embObj)

    @command
    async def deleteall(self, message: discord.Message) -> tuple:
        while len(self.last_MSG) > 0:
            try:
                await self.last_MSG.pop().delete()
            except:
                continue
        return (0, None)

    @command
    async def deletelast(self, message: discord.Message) -> tuple:
        args = message.content[1:].split(" ")
        if len(self.last_MSG) == 0:
            error = 3
        else:
            if len(args) > 1 and args[1].isnumeric:
                num_delete = int(args[1])
            else:
                num_delete = 1
            while num_delete > 0:
                if len(self.last_MSG) == 0:
                    break
                try:
                    await self.last_MSG.pop().delete()
                    num_delete -= 1
                except discord.NotFound:
                    continue
            error = 0
        return (error, None)

    @command
    async def easter(self, message: discord.Message) -> tuple:
        embObj = discord.Embed(
            title="What is this?",
            description="cmljZXB1cml0eXRlc3QubW9iaS9bZGlzY29yZG5hbWVfb2ZfMjIzOTMyNzc1NDc0OTIxNDcyXS5odG1s",
        )
        error = await self.sendMsg(toSend=embObj, channel=message.channel)
        await self.last_MSG.pop(-1).delete(delay=0.5)
        return (error, None)

    @command
    async def easterranks(self, message: discord.Message) -> tuple:
        try:
            txt = self.dbhandler.get_from_misc("easter")
            embObj = discord.Embed(title="Easter Egg Hunt leaderboard", description=txt)
            return (0, embObj)
        except OperationalError:
            embObj = discord.Embed(
                title="Easter Egg Hunt leaderboard",
                description="-- Something went wrong with DB --",
                color=self.ERRORCOLOR,
            )
            return (1, embObj)

    @command
    async def endtrack(self, message: discord.Message) -> tuple:
        toTrackID = 0
        toTrackName = "nobody"
        self.msgs.set_user(toTrackName)
        embObj = discord.Embed(
            title="Tracker", description="stopped tracking", color=self.TRACKERCOLOR
        )
        return (0, embObj)

    @command
    async def execsql(self, message: discord.Message) -> tuple:
        cont = message.content
        origlen = len(cont[1:].split(" ")[0].lower())
        query = cont[(origlen + 1) :].strip()
        try:
            res = self.dbhandler._execComm(query)
        except OperationalError as e:
            logger.error(f"Something went wrong with the DB (Query: {query} ")
            # print("[commandhandler.py] Something went wrong with sqlite")
            embObj = discord.Embed(
                title="ExecSQL", description=str(e), color=self.ERRORCOLOR
            )
            return (3, embObj)  # command is fuckd up probably
        if res != -10:
            embObj = discord.Embed(
                title="Query Result", description=">" + query, color=self.QUERYCOLOR
            )
            embed_len = 100
            if len(res) > self.FIELDSIZELIMIT:
                res2 = res.split("\n")
                curr_page_num = 1
                curr_page_cont = ""
                for line in res2:
                    if line.strip() == "":
                        continue
                    if len(curr_page_cont + line[:100]) + 2 > self.FIELDSIZELIMIT:
                        embed_len += len(curr_page_cont[:100])
                        if embed_len > self.EMBEDSIZELIMIT:
                            break
                        embObj.add_field(
                            name=f"Page {curr_page_num}",
                            value=curr_page_cont[: self.FIELDSIZELIMIT],
                            inline=False,
                        )
                        curr_page_cont = line[:100] + "\n"
                        curr_page_num += 1
                    else:
                        curr_page_cont += line[:100] + "\n"
                if (
                    len(curr_page_cont) > 0
                    and embed_len + len(curr_page_cont) <= self.EMBEDSIZELIMIT
                ):
                    embObj.add_field(
                        name=f"Page {curr_page_num}",
                        value=curr_page_cont[: self.FIELDSIZELIMIT],
                    )
            else:
                embObj.add_field(name="Output", value=res)
            return (0, embObj)
        else:
            return (0, None)

    @command
    async def fixissue(self, message: discord.Message) -> tuple:
        args = message.content[1:].split(" ")
        try:
            arg = int(args[1])
            self.dbhandler.fixissue(arg)
            error = 0
        except IndexError:
            error = 3
        return (error, None)

    @command
    async def getmemes(self, message: discord.Message) -> tuple:
        memes = meme.get_popular_memes()
        embObj = discord.Embed(title="currently popular memes", color=self.MISCCOLOR)
        pagecount = 0
        curr_page_cont = ""
        for name, id in memes:
            if len(curr_page_cont + name + str(id)) + 5 <= self.FIELDSIZELIMIT:
                curr_page_cont += f"{name} -> {id}\n"
            else:
                pagecount += 1
                embObj.add_field(name=f"Page {pagecount}", value=curr_page_cont)
                curr_page_cont = f"{name} -> {id}\n"
                if pagecount > 5:
                    break

        return (0, embObj)

    @command
    async def gettrack(self, message: discord.Message) -> tuple:
        embObj = discord.Embed(
            title="Tracker",
            description=f"currently tracking {self.toTrackName}",
            color=self.TRACKERCOLOR,
        )
        return (0, embObj)

    @command
    async def ga(self, message: discord.Message) -> tuple:
        dm_chan = await message.author.create_dm()  # type: discord.DMChannel
        dm_emb_obj = discord.Embed(
            title="Average of tracked guesses",
            description=f"Result: {self.dbhandler.get_avg_guess(message.author.id)}",
        )
        await dm_chan.send(embed=dm_emb_obj)
        emb_obj = discord.Embed(
            title="Magic feature", description="You should've gotten a dm <3"
        )
        return 0, emb_obj

    @command
    async def help(self, message: discord.Message) -> tuple:
        try:
            channel = message.channel
            args = message.content[1:].split(" ")
            permlevel = self.dbhandler.get_perm_level(message.author.id)

            if len(args) > 1 and args[1].isnumeric:
                permlevel = int(args[1])
            cmds = self.dbhandler._execComm(
                """SELECT cmdname,helptext,alias,permlevel from commands where enabled==1 ORDER BY cmdname ASC, permlevel ASC""",
                raw=True,
            )
            emotes = self.dbhandler._execComm(
                """SELECT value,desc FROM emotes ORDER BY id ASC""", raw=True
            )
            final_cmd = []
            for c in cmds:
                if c[3] <= permlevel:
                    final_cmd.append((c[0], c[1], c[2]))
            embObj = discord.Embed(
                title="Help",
                description="Displaying all available commands depending on callees permissionlevel",
                color=self.SYSTEMCOLOR,
            )

            txt = []
            currFieldCont = ""
            currFieldIndex = 1
            for (cmdn, text, alias) in final_cmd:
                txt = f'`{self.PREFIX}{cmdn}` (`{self.PREFIX}{alias}`)\t {text.replace("_"," ")}\n'
                if len(currFieldCont + txt) > self.FIELDSIZELIMIT:
                    embObj.add_field(name=f"Page {currFieldIndex}", value=currFieldCont)
                    currFieldIndex += 1
                    currFieldCont = txt
                else:
                    currFieldCont += txt
            if currFieldCont == "" and currFieldIndex == 1:
                currFieldCont = "[Well.. nothing :/]"  # lol
            embObj.add_field(name=f"Page {currFieldIndex}", value=currFieldCont)
            emote_val = ""
            for (emote, desc) in emotes:
                emote_val += f"{emote}\t{desc}\n"
            embObj.add_field(name="Emotes", value=emote_val, inline=False)
            return (0, embObj)
        except Exception as e:
            embObj = discord.Embed(
                title="Help", description=str(e), color=self.ERRORCOLOR
            )
            return (1, embObj)

    @command
    async def info(self, message: discord.Message) -> tuple:
        try:

            embObj = discord.Embed(
                title=self.client.user.name,
                description="Info about the greatest bot",
                color=self.SYSTEMCOLOR,
                url="http://brrr.nighmared.tech",
            )
            if int(self.dbhandler.get_from_misc("debug")) > 0:
                embObj.add_field(
                    name="TESTING DEPLOYMENT", value=f"Prefix: `{self.PREFIX}`"
                )
            embObj.set_thumbnail(
                url="https://repository-images.githubusercontent.com/324449465/a07d7880-4890-11eb-8bfa-a5db39975455"
            )
            # 	embObj.set_author(name="joniii")
            embObj.add_field(name="Author", value="<@!291291715598286848>")
            embObj.add_field(name="GH Repo", value="http://brrr.nighmared.tech")
            embObj.add_field(
                name="Version <a:cheer:824995182607990824>",
                value=f"`{self.dbhandler.get_from_misc('version')}`",
                inline=False,
            )
            embObj.add_field(
                name="discord.py Version",
                value=f"`{discord.version_info.major}.{discord.version_info.minor}.{discord.version_info.micro}`",
            )
            embObj.add_field(
                name="Python Version",
                value=f"`{python_version.major}.{python_version.minor}.{python_version.micro}`",
            )
            embObj.add_field(
                name="Uptime",
                value="`" + self.uptime_tracker.get_uptime() + "`",
                inline=False,
            )

            return (0, embObj)
        except Exception as e:
            embObj = discord.Embed(
                title="Info", description=str(e), color=self.ERRORCOLOR
            )
            return (1, embObj)

    @command
    async def inspire(self, message: discord.Message) -> tuple:
        error, cont = inspirobot.get_img_url()
        if error > 0:
            embObj = discord.Embed(
                title="Inspire", description=cont, color=self.ERRORCOLOR
            )
        else:
            embObj = discord.Embed(
                title="Inspire",
                description="Newly generated inspirobot.me quote",
                url="https://inspirobot.me",
                color=self.MISCCOLOR,
            )
            embObj.set_image(url=cont)
        return (error, embObj)

    @command
    async def loopstatus(self, message: discord.Message) -> tuple:
        def time_string(time_diff: int) -> str:
            hours = int(time_diff / 3600)
            time_diff %= 3600
            mins = int(time_diff / 60)
            time_diff %= 60
            if hours > 0:
                if mins > 0:
                    return f"{hours}h {mins}m"
                return f"{hours}h"
            elif mins > 0:
                if time_diff > 0:
                    return f"{mins}m {time_diff}s"
                return f"{mins}m"
            else:
                return f"{time_diff}s"

        try:
            loops = self.dbhandler.get_loops()
        except OperationalError:
            logger.error("getting loop info from db went wrong")
            return 1, None
        curr_time = int(current_time_sec())
        emb_obj = discord.Embed(
            title="Loops",
            description="How long since each loop was last seen alive",
            color=self.SYSTEMCOLOR,
        )
        for loopname, lastseen, freq in loops:
            emb_obj.add_field(
                name=loopname,
                value=f"{time_string(curr_time-lastseen)} (should be ≤ {time_string(freq)})",
                inline=True,
            )

        return 0, emb_obj

    @command
    async def makememe(self, message: discord.Message) -> tuple:
        try:
            probable_sqli = message.content.count('"') > 2
            space_split_args = message.content.split(" ")
            caption = message.content.split('"')[1]
            for x in ("'", "--", ";", "*", "ʼ"):
                if x in caption:
                    probable_sqli = True
                    break

            if probable_sqli:
                embObj = discord.Embed(
                    title="makememe",
                    description=f"This seems sus af..{self.dbhandler.get_emote(emote_id=1)}",
                    color=self.QUERYCOLOR,
                )
                embObj.add_field(name="WHODIDTHIS", value=message.author.mention)
                embObj.add_field(name="command", value=message.content[:2000])
                embObj.add_field(name="Tag for easy search", value="GGB SQLI")
                return (3, embObj)
            template_name = space_split_args[1]
            top_caption = False
            text0 = text1 = ""
            crosssplit = caption.split("#")
            text0 = crosssplit[0]
            if len(crosssplit) > 1:
                text1 = crosssplit[1]
            error, img_url, error_descr, post_url = meme.get_meme(
                template_name, text0, text1, self.dbhandler
            )
        except IndexError:
            error = 3
            error_descr = "Invalid Usage"
        if error == 3:  # -> invalid template
            embObj = discord.Embed(
                title="makememe", description=error_descr, color=self.ERRORCOLOR
            )
            templates = ""
            page = 1
            for t in self.dbhandler.get_meme_templates().keys():
                if len(templates + t) + 3 > self.FIELDSIZELIMIT:
                    embObj.add_field(name=f"Templates Page {page}", value=templates)
                    page += 1
                    templates = ""
                templates += t + ",  "
            embObj.add_field(name=f"Templates Page {page} ", value=templates)
            embObj.add_field(
                name="Usage",
                value=f'{self.PREFIX}makememe <template_name>  "upper caption # lower caption"\n Example:\n {self.PREFIX}makememe spongebob_mocking "spam is not nsfw" \n {self.PREFIX}makememe drake "studying # adding dumb features to my bot"',
                inline=False,
            )
            return (3, embObj)
        elif error == 1:
            embObj = discord.Embed(
                title="makememe", description=error_descr, color=self.ERRORCOLOR
            )
            return (1, embObj)
        else:
            self.dbhandler.add_meme(
                uid=message.author.id,
                img_url=img_url,
                caption=caption,
                template_name=template_name,
            )
            embObj = discord.Embed(
                title="makememe",
                description="Here's your meme",
                color=self.MISCCOLOR,
                url=post_url,
            )
            embObj.set_image(url=img_url)
            return (0, embObj)

    @command
    async def mostmessages(self, message: discord.Message) -> tuple:
        try:
            res = self.dbhandler.get_most_messages()
            embObj = discord.Embed(
                title="Message Leaderboard",
                description="Showing which user has sent the most messages\n [Tracking started on 18.01.2021]",
                color=self.TRACKERCOLOR,
            )
            field_value = ""
            rank = 1
            for entry in res:
                to_add = f"{str(rank).rjust(3)}. {str(entry[0]).rjust(32)} {str(entry[1]).rjust(5)}\n"
                if len(field_value + to_add) > self.FIELDSIZELIMIT:
                    embObj.add_field(name=f"Ranking", value=field_value, inline=False)
                    field_value = ""
                    break
                else:
                    field_value += to_add
                rank += 1
            if field_value != "":
                embObj.add_field(name=f"Ranking", value=field_value, inline=False)
            return (0, embObj)
        except Exception as e:
            embObj = discord.Embed(
                title="Message Leaderboard", description=str(e), color=self.ERRORCOLOR
            )
            return (1, embObj)

    @command
    async def msgarchive(self, message: discord.Message) -> tuple:
        try:
            msgls = self.msgs.sendable()
            if len(msgls) == "":
                error = 2
            else:
                embObj = discord.Embed(
                    title="Tracker",
                    description=f"Recent messages by {msgls[0].author.nick}",
                    color=self.TRACKERCOLOR,
                )
                fieldStr = ""
                for msg in msgls:
                    fieldStr += f"{str(msg.created_at)[:-4]} {msg.author.nick}-> {msg.channel.name}: {msg.content[:100]}\n"
                embObj.add_field(name="Messagehistory", value=fieldStr, inline=True)
            return (0, embObj)
        except Exception as e:
            embObj = discord.Embed(
                title="Tracker",
                description=f"Something went wrong, prolly not tracking anyone rn \n➥{str(e)}",
                color=self.ERRORCOLOR,
            )
            return (1, embObj)

    @command
    async def neko(self, message: discord.Message) -> tuple:
        try:
            embObj = discord.Embed(
                title="Neko", description=neko.getNeko(), color=self.MISCCOLOR
            )
            return (0, embObj)
        except Exception as e:
            embObj = discord.Embed(
                title="Neko", description=str(e), color=self.ERRORCOLOR
            )
            return (1, embObj)

    @command
    async def newprefix(self, message: discord.Message) -> tuple:
        args = message.content.split(" ")
        error = 0
        if len(args) != 2:
            error = 3
            errormsg = "Mismatch in number of args given."
        newprefix = args[1]
        if len(newprefix) != 1:
            error = 3
            errormsg = "Prefix may only be one character long!"

        if error == 0:
            try:
                self.dbhandler.set_to_misc("prefix", newprefix)
                self.PREFIX = newprefix
                error = 77
                emb_obj = discord.Embed(
                    title="Prefix updated",
                    description=f"new Prefix: {newprefix}",
                    color=self.SYSTEMCOLOR,
                )
            except OperationalError as e:
                error = 1
                errormsg = str(e)

        if error == 3:
            emb_obj = discord.Embed(
                title="You did something wrong",
                description=errormsg,
                color=self.ERRORCOLOR,
            )
            emb_obj.add_field(
                name="Usage",
                value=f"{self.PREFIX} <new prefix> \n Example: `{self.PREFIX}newprefix °`",
            )
        if error == 1:
            emb_obj = discord.Embed(
                title="DB Error...", description=errormsg, color=self.ERRORCOLOR
            )

        return error, emb_obj

    @command
    async def nhentai(self, message: discord.Message) -> tuple:
        PROTECTED_SERVERS = (747752542741725244,)
        if not (
            type(message.channel) != discord.channel.TextChannel
            or message.channel.is_nsfw()
        ):
            return (2, None, None)

        if message.guild and message.guild.id in PROTECTED_SERVERS:
            embObj = discord.Embed(
                title="nHentai Random Cover",
                description="nonononono",
                color=self.MISCCOLOR,
                url="https://http.cat/451",
            )
            embObj.set_image(url="https://http.cat/451")
            file_to_send = None
            return (0, embObj, file_to_send)

        args = message.content[1:].split(" ")
        user_pl = self.dbhandler.get_perm_level(message.author.id)
        nsfw = (
            int(self.dbhandler.get_from_misc("nsfw")) != 0
            or type(message.channel) == discord.channel.DMChannel
        )
        link = ""
        error = 0
        img_id = -1
        sigma = int(self.dbhandler.get_from_misc("blur_sigma"))

        if (
            len(args) > 1
            and args[1].isnumeric
            and user_pl > self.dbhandler.get_cmd_perm("nhentai")
        ):
            img_id = args[1]
            link = self.dbhandler.get_nhentai_path_by_id(img_id, ignore_block=nsfw)[0]
            if link == -1:
                link = self.nh_handler.get_img(sigma, img_id)
        else:
            sigma = int(self.dbhandler.get_from_misc("blur_sigma"))
            link = self.nh_handler.get_img(sigma)
        if error == 0:
            if nsfw:
                link = f"{link.rstrip('.blurred.jpg')}.jpg"
            img_id = link.rstrip(".blurred.jpg")
            url = "https://http.cat/451"

            if message.guild and message.guild.id not in PROTECTED_SERVERS:
                url = f"https://nhentai.net/g/{img_id.lstrip('nhentai/')}"
            embObj = discord.Embed(
                title="nHentai Random Cover",
                description=img_id,
                color=self.MISCCOLOR,
                url=url,
            )

            try:
                file_to_send = discord.File(
                    link, filename="SPOILER_FILE.jpg", spoiler=True
                )
            except FileNotFoundError:  # accidentally pushed dumb shit; this will rarely occur but prolly fixes it
                link2 = link.rstrip(".blurred.jpg") + ".jpg"
                self.nh_handler._blur(link2, sigma)
                file_to_send = discord.File(
                    link, filename="SPOILER_FILE.jpg", spoiler=True
                )
            embObj.set_image(url="attachment://SPOILER_FILE.jpg")
            nh_log = open("nhentai/log.txt", "a")
            nh_log.write(f">Sent nhentai/{str(img_id).lstrip('nhentai/')}\n")
            nh_log.close()
        return (0, embObj, file_to_send)

    @command
    async def nhentaiblock(self, message: discord.Message) -> tuple:
        args = message.content[1:].replace("  ", " ").split(" ")
        if len(args) > 1 and args[1].isnumeric:
            error = self.nh_handler.nhentai_block(args[1])
        else:
            error = 3
        return (error, None)

    @command
    async def nhentailog(self, message: discord.Message) -> tuple:
        try:
            log_len = min(int(self.dbhandler.get_from_misc("nh_log_len")), 48)
            with open("nhentai/log.txt") as log_file:
                log_lines = log_file.readlines()
            embObj = discord.Embed(title="nhentai log", color=self.MISCCOLOR)
            field_cont = ""
            for line in log_lines[-log_len:]:
                field_cont += line
            embObj.add_field(name="Entries", value=field_cont)
            # log management
            if len(log_lines) > 500:
                logger.info("trying to rotate nh log")
                open("nhentai/log.txt.old", "w").writelines(
                    log_lines
                )  # lol idk how this is gonna end
                curr_log = open("nhentai/log.txt", "w")
                curr_log.write("")
                curr_log.close()

            return (0, embObj)
        except Exception as e:
            embObj = discord.Embed(
                title="nhentai log", description=str(e), color=self.ERRORCOLOR
            )
            return (1, embObj)

    @command
    async def ping(self, message: discord.Message) -> tuple:
        embObj = discord.Embed(
            title="Ping", description="Pong!", color=self.SYSTEMCOLOR
        )
        embObj.add_field(name="Ping", value="TBA ms")
        embObj.add_field(
            name="Latency", value=str(self.client.latency * 1000)[:5] + "ms"
        )
        callee = (
            message.author.name if message.author.nick is None else message.author.nick
        )
        embObj.set_author(name=callee, icon_url=message.author.avatar_url)
        embObj.timestamp = self.uptime_tracker.get_now_utc()
        channel = message.channel

        a = self.uptime_tracker.get_now_utc()  # measure time it takes to send msg
        x = await channel.send(embed=embObj)
        b = self.uptime_tracker.get_now_utc()
        self.last_MSG.append(x)  # cuz not automatically added kek
        ping_in_ms = (b - a).total_seconds() * 1000  # compute ms of timedelta

        embObj.set_field_at(0, name="Ping", value=f"{int(ping_in_ms)} ms")
        await x.edit(embed=embObj)  # refresh value in sent msg
        return (0, None)  # nothing to return as already sent

    @command
    async def polyreload(self, message: discord.Message) -> tuple:
        try:
            self.dbhandler.update_polyring_feeds(
                polyring.update_feeds(), command_user_id=message.author.id
            )
            return (0, None)
        except Exception as e:
            logger.error(str(e))
            return (1, None)

    @command
    async def pubkey(self, message: discord.Message) -> tuple:
        embObj = discord.Embed(title="PUBLIC KEY", color=0x000000)
        file = discord.File("joniii.pub")
        return (0, embObj, file)

    @command
    async def reload(self, message: discord.Message) -> tuple:
        embObj = discord.Embed(
            title="Reloading...",
            description="let's hope this doesn't fuck anything up...",
            color=self.SYSTEMCOLOR,
        )
        return (99, embObj)

    @command
    async def reloadissues(self, message: discord.Message) -> tuple:
        try:
            ls = issues.getIssues()
            if ls[0][0] == -1:
                error = 1
            else:
                self.dbhandler._execComm("DELETE FROM issues")
                for issue in ls:
                    self.dbhandler.add_issue(issue)

            embObj = discord.Embed(
                title="Issues", description="Issues reloaded", color=self.ISSUECOLOR
            )
            return (0, embObj)
        except Exception as e:
            embObj = discord.Embed(
                title="Issues", description=str(e), color=self.ERRORCOLOR
            )
            return (1, embObj)

    @command
    async def robohash(self, message: discord.Message) -> tuple:
        command_len = len(message.content.split(" ")[0])
        return (0, robohash.get_embed(message.content[command_len:].strip()))

    @command
    async def say(self, message: discord.Message) -> tuple:
        channel = message.channel
        args = message.content[1:].split(" ")
        resttxt = ""
        for a in args[1:]:
            resttxt += " " + a
        parts = resttxt.split("#")
        text = parts[0]
        try:
            repnum = int(parts[1])
        except:
            repnum = 0
        error = await self.sendMsg(channel, f"{text}")
        for counter in range(0, repnum):
            await self.sendMsg(channel, f"{text}")
        return (error, None)

    @command
    async def setcache(self, message: discord.Message) -> tuple:
        args = message.content[1:].split(" ")
        cachelen = args[1]

        try:
            newLen = int(cachelen)
            newLen = self.msgs.set_len(newLen)
            embObj = discord.Embed(
                title="Tracker",
                description=f"updated cache length to {newLen}",
                color=self.TRACKERCOLOR,
            )
            return (0, embObj)
        except Exception as e:
            embObj = discord.Embed(
                title="Tracker", description=str(e), color=self.ERRORCOLOR
            )
            return (1, embObj)

    @command
    async def setchangelog(self, message: discord.Message) -> tuple:
        try:
            args = message.content[1:].split(" ")
            new_changelog = " ".join(args[1:])
            self.dbhandler.set_to_misc("changelog", new_changelog)
            return (0, None)
        except Exception as e:
            embObj = discord.Embed(
                title="setchangelog", description=str(e), color=self.ERRORCOLOR
            )
            logger.error("Something got fucked up when handling setchangelog")
            # print("[commandhandler.py] UWU SHIT GONE WRONG IN SCL HANDLING")
            return (1, embObj)

    @command
    async def setperm(self, message: discord.Message) -> tuple:
        own_perm_lev = self.dbhandler.get_perm_level(message.author.id)
        user = message.mentions[0]
        args = message.content[1:].replace("  ", " ").split(" ")
        perm_lev = args[2]
        if int(perm_lev) >= own_perm_lev:
            embObj = discord.Embed(
                title="setperm",
                description="Can't set others permission >= your own",
                color=self.ERRORCOLOR,
            )
            error = 3  # make sure you cant promote yourself or anyone else over your own rank
        else:
            try:
                error = self.dbhandler.set_perm(user, newpermlev=perm_lev)
                embObj = discord.Embed(
                    title="setperm",
                    description=f"{user.nick} now has permission level {perm_lev}",
                    color=self.SYSTEMCOLOR,
                )
            except Exception as e:
                error = 1
                embObj = discord.Embed(
                    title="setperm", description=str(e), color=self.ERRORCOLOR
                )
        return (error, embObj)

    @command
    async def setstatus(self, message: discord.Message) -> tuple:
        try:
            cont = message.content
            args = cont[1:].split(" ")
            type = 1
            error = 0
            splitbyquot = cont.split('"')
            if len(splitbyquot) not in (2, 3):
                if len(args) < 2:
                    return (3, None)  # u fucked up
                else:
                    stringarg = args[1]
                if len(args) > 2 and args[2].isnumeric():
                    type = args[2]
            else:
                stringarg = splitbyquot[1]
                if len(splitbyquot) == 3 and splitbyquot[2].strip().isnumeric():
                    type = int(splitbyquot[2])
            await self.client.change_presence(
                activity=discord.Activity(name=stringarg, type=type)
            )
            return (0, None)
        except Exception as e:
            embObj = discord.Embed(
                title="setstatus", description=str(e), color=self.ERRORCOLOR
            )
            return (1, embObj)

    @command
    async def settrack(self, message: discord.Message) -> int:
        try:
            user = message.mentions[0]
            self.toTrackID = user.id
            self.toTrackName = user.mention
            self.msgs.set_user(self.toTrackName)
            embObj = discord.Embed(
                title="Tracker",
                description=f"updated tracked user to {self.toTrackName}",
                color=self.TRACKERCOLOR,
            )
            return (0, embObj)
        except Exception as e:
            embObj = discord.Embed(
                title="Settrack", description=str(e), color=self.ERRORCOLOR
            )
            return (1, embObj)

    @command
    async def setversion(self, message) -> tuple:
        try:
            args = message.content[1:].split(" ")
            version = args[1]
            self.dbhandler.set_to_misc("version", version)
            embObj = discord.Embed(
                title="setversion",
                description=f"Version is now set to {version}",
                color=self.SYSTEMCOLOR,
            )
            return (0, embObj)
        except Exception as e:
            embObj = discord.Embed(
                title="setversion", description=str(e), color=self.ERRORCOLOR
            )
            return (1, embObj)

    @command
    async def shortlink(self, message) -> tuple:
        try:
            url_arg = message.content[1:].split(" ")[1]
        except IndexError:
            embObj = discord.Embed(
                title="Link Shortener",
                description="Missing argument `url`",
                color=self.ERRORCOLOR,
            )
            return (3, embObj)
        error, res = shorten.shorten_link(url_arg)
        embObj = discord.Embed(
            title="Link Shortener",
            description=res,
            color=(self.MISCCOLOR, self.ERRORCOLOR)[error],
        )
        return (error, embObj)

    @command
    async def showissues(self, message: discord.Message) -> tuple:
        try:

            res = self.dbhandler._execComm(
                "select * from issues", True
            )  # FIXME add a func in dbhandler to do this! NO DIRECT EXECS OUTSIDE OF DBHANDLER!!!!
            embObj = discord.Embed(title="Issues", color=self.ISSUECOLOR)
            for id, title, tags in res:
                if tags is not None:
                    tags_l = tags.split(";")
                else:
                    tags_l = []
                tags_s = ""
                for tag in tags_l:
                    if tag.strip() == "":
                        continue
                    tags_s += f"`{tag.strip()}` "
                if tags_s == "":
                    tags_s = "[No Tags]"
                embObj.add_field(name=f"{id}. {title}", value=tags_s, inline=False)
            # FIXME this doesnt work with discord caching, instead use github api to check workflow status and send static failed/passed image based on that
            badge_link = issues.get_badge_link()
            embObj.set_thumbnail(url=badge_link)
            return (0, embObj)
        except Exception as e:
            embObj = discord.Embed(
                title="Issues", description=str(e), color=self.ERRORCOLOR
            )
            return (1, embObj)

    @command
    async def showsourcecode(self, message: discord.Message) -> tuple:
        error = 0
        args = message.content[1:].split(" ")
        if len(args) < 2:
            embObj = discord.Embed(
                title="showsourcecode",
                description="Missing argument, use one of the following",
            )
            val_string = ""
            for fname in self.ALLOWEDSOURCEFILES.keys():
                val_string += fname + ", "
            embObj.add_field(name="Files available for display", value=val_string)
            return (3, embObj)
        else:
            module_name = args[1]
            if module_name in self.ALLOWEDSOURCEFILES.keys():
                line_indx = 0
                file = open(self.ALLOWEDSOURCEFILES[module_name], mode="r")
                lines = file.read().split("\n")
                file.close()
                num_lines = len(lines)
                syntax_keyword = (
                    "py"
                    if self.ALLOWEDSOURCEFILES[module_name].endswith("py")
                    else "sh"
                )
                if len(args) > 2 and args[2].isnumeric:
                    line_indx = int(args[2])  # start at later line
                if line_indx >= num_lines:
                    error = 3
                else:
                    msg = f"{'`'*3}{syntax_keyword}\n"
                    while line_indx < num_lines and len(msg + lines[line_indx]) < 1930:
                        msg += f"{str(line_indx+1).rjust(3)}| {lines[line_indx]}\n"
                        line_indx += 1
                    msg += "\n" + "`" * 3
                    caller_name: str = message.author.nick
                    caller_name = caller_name.translate(
                        {ord("@"): "\@", ord("#"): "\#", ord("<"): "\<", ord(">"): "\>"}
                    )
                    msg += f"> Answering to {caller_name}"
                    return (0, msg)
            else:
                return (4, None)
        return (error, None)

    @command
    async def source(self, message: discord.Message) -> tuple:
        return (
            0,
            discord.Embed(
                title="Source",
                description="http://brrr.nighmared.tech",
                color=self.SYSTEMCOLOR,
            ),
        )

    @command
    async def stalk(self, message: discord.Message) -> tuple:
        def make_date_nice(date) -> str:
            return date.strftime("`%A, %d %B %Y, %H:%M`")

        args = message.content[1:].split(" ")
        try:
            target_id = args[1]
        except IndexError:
            target_id = message.author.id
        t_id = int(target_id)
        try:
            try:  # id belongs to a member of the guild
                target = await message.guild.fetch_member(target_id)
                embObj = discord.Embed(
                    title="Stalking | User",
                    description=f"Info about {target.mention}",
                    color=self.TRACKERCOLOR,
                )
                embObj.add_field(
                    name="Username", value=f"{target.name}#{target.discriminator}"
                )
                embObj.add_field(name="UID", value=target.id, inline=False)
                embObj.add_field(
                    name="Account Created",
                    value=make_date_nice(target.created_at),
                    inline=False,
                )
                embObj.add_field(
                    name="Joined Server",
                    value=make_date_nice(target.joined_at),
                    inline=False,
                )
                embObj.add_field(name="Is bot", value=target.bot)
                embObj.add_field(name="Highest Role", value=target.top_role.mention)
                embObj.set_image(url=target.avatar_url)
                embObj.set_thumbnail(url=message.guild.icon_url)
            except NotFound:  # id belongs to a non-member user
                try:
                    target = await self.client.fetch_user(target_id)
                    embObj = discord.Embed(
                        title="Stalking | User",
                        description=f"Info about {target.mention}",
                        color=self.TRACKERCOLOR,
                    )
                    embObj.add_field(
                        name="Username", value=f"{target.name}#{target.discriminator}"
                    )
                    embObj.add_field(name="UID", value=target.id, inline=False)
                    embObj.add_field(
                        name="Account Created", value=make_date_nice(target.created_at)
                    )
                    embObj.add_field(name="Is bot", value=target.bot)
                    embObj.set_image(url=target.avatar_url)
                except NotFound:  # id belongs to a channel

                    try:
                        try:
                            target = await self.client.fetch_channel(target_id)
                        except Forbidden:
                            target = list(
                                filter(
                                    lambda x: x.id == t_id,
                                    await message.guild.fetch_channels(),
                                )
                            )[0]
                        embObj = discord.Embed(
                            title="Stalking | Channel",
                            description=f"Info about {target.mention}",
                            color=self.TRACKERCOLOR,
                        )
                        embObj.add_field(name="Channel Name", value=target.name)
                        if isinstance(target, discord.TextChannel):
                            attrs = " None "
                            if target.is_nsfw():
                                attrs = "NSFW "
                            if target.is_news():
                                attrs += " NEWS "
                            embObj.add_field(
                                name="Special Attributes", value=str(attrs)
                            )
                            embObj.add_field(name="Topic", value=target.topic)
                            embObj.add_field(
                                name="Category", value=target.category.mention
                            )

                        elif isinstance(target, discord.VoiceChannel):  # voice channel
                            embObj.add_field(name="Bitrate", value=target.bitrate)
                            embObj.add_field(name="Max User #", value=target.user_limit)
                            embObj.add_field(
                                name="Category", value=target.category.mention
                            )

                        else:  # category channel
                            embObj.add_field(name="NSFW", value=target.is_nsfw())
                            txt_chans = [x.mention for x in target.text_channels]
                            vic_chans = [x.mention for x in target.voice_channels]
                            if len(txt_chans) > 0:
                                embObj.add_field(name="Text Channels", value=txt_chans)
                            if len(vic_chans) > 0:
                                embObj.add_field(name="Voice Channels", value=vic_chans)

                        embObj.add_field(name="Server", value=target.guild.name)
                        embObj.add_field(
                            name="Created at", value=make_date_nice(target.created_at)
                        )
                        embObj.set_thumbnail(url=target.guild.icon_url)

                    except NotFound:  # guild
                        try:
                            target = await self.client.fetch_guild(target_id)
                            embObj = discord.Embed(
                                title="Stalking | Server",
                                description=f"Info about {target.name}",
                                color=self.TRACKERCOLOR,
                            )
                            embObj.add_field(
                                name="Boosts", value=target.premium_subscription_count
                            )
                            embObj.add_field(
                                name="Boost Level", value=target.premium_tier
                            )
                            embObj.add_field(
                                name="Description",
                                value=target.description,
                                inline=False,
                            )
                            embObj.add_field(
                                name="Created at",
                                value=make_date_nice(target.created_at),
                                inline=False,
                            )
                            embObj.add_field(
                                name="Owner",
                                value=(
                                    await self.client.fetch_user(target.owner_id)
                                ).mention,
                            )
                            embObj.add_field(
                                name="Max Members", value=f"{target.max_members} "
                            )
                            embObj.add_field(
                                name="Region", value=str(target.region).capitalize()
                            )
                            role_str = ""
                            for role in target.roles[::-1]:
                                if len(role_str + role.mention) > 512:
                                    role_str += "..."
                                    break
                                role_str += f"{role.mention} "
                            embObj.add_field(name="Roles", value=role_str, inline=False)
                            embObj.set_thumbnail(url=message.guild.icon_url)
                            embObj.set_image(url=message.guild.banner_url)
                        except (NotFound, Forbidden):  # role?
                            try:
                                target = list(
                                    filter(lambda x: x.id == t_id, message.guild.roles)
                                )[0]
                            except IndexError:
                                target = None
                            if target is None:
                                embObj = discord.Embed(
                                    title="Stalking | ...what is this?",
                                    description=f"Couldnt find out what {target_id} represents.. sawry\n Probably a Server the bot has no access to",
                                    color=self.ERRORCOLOR,
                                )
                            else:  # yup role
                                embObj = discord.Embed(
                                    title="Stalking | Role",
                                    description=f"Info about {target.mention}",
                                    color=self.TRACKERCOLOR,
                                )
                                embObj.add_field(name="Color", value=str(target.color))
                                embObj.add_field(
                                    name="Pingable", value=target.mentionable
                                )
                                embObj.add_field(
                                    name="Default role", value=target.is_default()
                                )
                                embObj.add_field(name="Position", value=target.position)
                                embObj.add_field(
                                    name="Created at",
                                    value=make_date_nice(target.created_at),
                                    inline=False,
                                )
                                embObj.set_thumbnail(url=message.guild.icon_url)

            return (0, embObj)
        except Exception as e:
            traceback.print_exc()
            embObj = discord.Embed(
                title="Stalking",
                description=str(e) + str(type(e)),
                color=self.ERRORCOLOR,
            )
            return (1, embObj)

    @command
    async def superdelete(self, message: discord.Message) -> tuple:
        target_msg = await message.channel.fetch_message(message.reference.message_id)
        embObj = None
        try:
            await target_msg.delete()
            error = 0
        except discord.Forbidden:
            error = 4
        except discord.NotFound:
            error = 2
        except discord.HTTPException:
            error = 1
        except Exception as e:
            embObj = discord.Embed(
                title="Superdelete", description=str(e), color=self.ERRORCOLOR
            )
        return (error, None)

    @command
    async def togglecmd(self, message: discord.Message) -> tuple:
        try:
            args = message.content[1:].split(" ")
            if args[1].strip() == "?":
                totogglecmd = "help"
            else:
                totogglecmd = ""
                totogglecmd = self.dbhandler.find_alias(args[1].strip())
            if totogglecmd.strip() == "":
                return (3, None)
            self.dbhandler._execComm(
                f'''UPDATE commands SET enabled={(1,0)[self.dbhandler.cmd_is_enabled(totogglecmd)]} WHERE cmdname=="{totogglecmd}"'''
            )
            return (0, None)
        except IndexError:
            embObj = discord.Embed(
                title="togglecmd",
                description=f"Usage: {self.PREFIX}togglecmd <cmdname>",
                color=self.ERRORCOLOR,
            )
            return (3, embObj)
        except Exception as e:
            embObj = discord.Embed(
                title="togglecmd", description=str(e), color=self.ERRORCOLOR
            )
            return (1, embObj)

    @command
    async def togglensfw(self, message: discord.Message) -> tuple:
        try:
            new_state = self.dbhandler.toggle_nsfw()
            embObj = discord.Embed(
                title="Toggled NSFW",
                color=self.MISCCOLOR,
                description=f"Turned explicit content {('off','on')[new_state]}",
            )
            return (0, embObj)
        except OperationalError:
            embObj = discord.Embed(
                title="togglensfw",
                description="-- Something wrong with DB --",
                color=self.ERRORCOLOR,
            )
            return (1, embObj)
        except Exception as e:
            embObj = discord.Embed(
                title="togglensfw", description=str(e), color=self.ERRORCOLOR
            )
            return (1, embObj)

    @command
    async def triggerannoy(self, message: discord.Message) -> tuple:
        try:
            self.dbhandler.set_to_misc(
                "annoyreaction", (not self.dbhandler.shouldAnnoy())
            )
            embObj = discord.Embed(
                title="Tracker",
                description=f" Turned reaction annoyance {('Off','On')[self.dbhandler.shouldAnnoy()]}",
                color=self.TRACKERCOLOR,
            )
            return (0, embObj)
        except Exception as e:
            embObj = discord.Embed(
                title="triggerannoy", description=str(e), color=self.ERRORCOLOR
            )
            return (1, embObj)

    @command
    async def xkcd(self, message: discord.Message) -> tuple:
        try:
            url_arg = message.content.split(" ")[1]
            res = xkcd.get_comic(int(url_arg))
            if res["success"]:
                embObj = discord.Embed(
                    title=f"xkcd/{res['num']}: {res['title']}",
                    color=self.MISCCOLOR,
                    url=f"https://xkcd.com/{res['num']}/",
                )
                embObj.set_image(url=res["img_url"])
                embObj.add_field(
                    name="Explanation",
                    value=f"https://www.explainxkcd.com/wiki/index.php/{res['num']}",
                )
                embObj.add_field(name="Alt", value=res["alt"], inline=False)
                return (0, embObj)
            else:
                embObj = discord.Embed(
                    title="Something went wrong when fetching the image..",
                    description=res["error"],
                    color=self.ERRORCOLOR,
                )
                return (1, embObj)

        except IndexError:  # no arg provided? aight just fetch latest
            res = xkcd.get_latest()
            if res["success"]:
                embObj = discord.Embed(
                    title=f"xkcd/{res['num']}: {res['title']}",
                    color=self.MISCCOLOR,
                    url=f"https://xkcd.com/{res['num']}/",
                )
                embObj.set_image(url=res["img_url"])
                embObj.add_field(
                    name="Explanation",
                    value=f"https://www.explainxkcd.com/wiki/index.php/{res['num']}",
                )
                embObj.add_field(name="Alt", value=res["alt"], inline=False)
                return (0, embObj)
            else:
                embObj = discord.Embed(
                    title="Something went wrong when fetching the image..",
                    description=res["error"],
                    color=self.ERRORCOLOR,
                )
                return (1, embObj)
        except ValueError:  # invalid arg (not numeric), throw error
            embObj = discord.Embed(
                title="xkcd",
                description="Invalid argument provided",
                color=self.ERRORCOLOR,
            )
            return (3, embObj)
