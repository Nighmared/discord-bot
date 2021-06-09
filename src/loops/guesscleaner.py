import logging
import discord.ext.commands
from discord.ext import tasks
from time import localtime,time


import dbhandler

IMPORTS = (dbhandler,)
logger = logging.getLogger("botlogger")

class GuessCleaner(discord.ext.commands.Cog):
	def __init__(self,client:discord.ext.commands.Bot, handler_ref):
		self.client = client
		self.handler_ref = handler_ref
		self.dbhandler = dbhandler.Dbhandler("discordbot.db") #type: dbhandler.Dbhandler

		self.cleaner.start()

	@tasks.loop(seconds=3600)
	async def cleaner(self):
		logger.info("Cleaner loop got called")
		ltime = localtime()
		if ltime.tm_hour == 13 and ltime.tm_wday<5:
			self.dbhandler.clean_guesses()
			logger.info("Guesses were purged")
		
		self.dbhandler.ping_loop("Magic Loop",time())
		