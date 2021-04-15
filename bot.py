
import logging
from re import split #for cmd handling
import discord # api library
from importlib import reload
from datetime import datetime
from sys import exit, argv
import subprocess as sub # needed for softreload to pull from git kekw
import msghandler #handle all incoming msgs


logger = logging.getLogger("botlogger")


with open(".token.txt") as t_file:
	TOKEN = t_file.read()

STARTTIME = datetime.now()
client = discord.Client()

msghandler.init(client,STARTTIME)





@client.event
async def on_ready():
	msghandler.ISRELOADING = False
	print(f'[bot.py] {client.user} has connected')
	logger.info("Bot Online")

@client.event
async def on_message(message:discord.Message):
	handling_code = await msghandler.handle(message)
	if handling_code == 99: #hard reload
		exit(0)
	elif handling_code == 88: #soft reload
		sub.run(["git","pull","--no-edit"]) # git pull --no-edit
		msgs_backup = msghandler.handler.last_MSG
		reload(msghandler)
		await msghandler.doreload(message,client=client,STARTTIME=STARTTIME,msgs_backup=msgs_backup)



if __name__ == "__main__" and len(argv)==1:
	client.run(TOKEN)
