#! /usr/bin/env python3
import logging
import subprocess as sub  # needed for softreload to pull from git kekw
from datetime import datetime
from importlib import reload
from sys import argv, exit

import discord  # api library
from discord.ext.commands import Bot

import handler  # handle all incoming msgs
import loophandler as loop

logger = logging.getLogger("botlogger")


FALLBACK_PREFIX = "°"

with open(".token.txt") as t_file:
    TOKEN = t_file.read()

STARTTIME = datetime.now()

# not using these parts of the discord library,
# so doesn't matter what prefix is given to the bot instance
client = Bot(FALLBACK_PREFIX)
handler.init(client, STARTTIME)


@client.event
async def on_ready():
    handler.ISRELOADING = False
    loop.init(client, handler_ref=handler)
    print(f"[bot.py] {client.user} has connected")
    logger.info("Bot Online")
    activity = discord.Activity(
        type=discord.ActivityType.listening,
        name=f"{handler.PREFIX}help",
        url="https://nighmared.tech",
    )
    await client.change_presence(status=discord.Status.idle, activity=activity)


@client.event
async def on_message(message: discord.Message):
    handling_code = await handler.handle(message)
    if handling_code == 99:  # hard reload
        exit(0)
    elif handling_code == 88:  # soft reload
        sub.run(["git", "pull", "--no-edit"])  # git pull --no-edit
        msgs_backup = handler.cmdhandler.last_MSG
        reload(handler)
        await handler.doreload(
            message, client=client, STARTTIME=STARTTIME, msgs_backup=msgs_backup
        )
        loop.init(client, handler)


if __name__ == "__main__" and len(argv) == 1:
    client.run(TOKEN)
