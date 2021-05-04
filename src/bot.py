
import logging
from re import split #for cmd handling
import discord # api library
from importlib import reload
from datetime import datetime
from sys import exit, argv
import subprocess as sub # needed for softreload to pull from git kekw
import handler #handle all incoming msgs
from discord.ext.commands import Bot
import loophandler as loop


logger = logging.getLogger("botlogger")


with open("PREFIX.txt") as prefix_file:
	PREFIX = prefix_file.read().strip()

with open(".token.txt") as t_file:
	TOKEN = t_file.read()

STARTTIME = datetime.now()

client = Bot(PREFIX)
handler.init(client,STARTTIME)





@client.event
async def on_ready():
	handler.ISRELOADING = False
	loop.init(client, handler_ref = handler)
	print(f'[bot.py] {client.user} has connected')
	logger.info("Bot Online")

@client.event
async def on_message(message:discord.Message):
	handling_code = await handler.handle(message)
	if handling_code == 99: #hard reload
		exit(0)
	elif handling_code == 88: #soft reload
		sub.run(["git","pull","--no-edit"]) # git pull --no-edit
		msgs_backup = handler.cmdhandler.last_MSG
		reload(handler)
		await handler.doreload(message,client=client,STARTTIME=STARTTIME,msgs_backup=msgs_backup)
		loop.init(client,handler)



if __name__ == "__main__" and len(argv)==1:
	client.run(TOKEN)
