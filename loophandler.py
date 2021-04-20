import discord
import discord.ext.commands
import logging
import loops.polyring as polyring
import handler

IMPORTS = (polyring,)
logger = logging.getLogger("botlogger")



def init(client: discord.ext.commands.Bot,handler_ref:handler):
	
	LOOPCOGS = (
		polyring.PolyringFetcher,
	)
	
	logger.info("adding cogs")
	for cog in LOOPCOGS:
		client.add_cog(cog(client,handler_ref))


def discard(client:discord.ext.commands.Bot):
	cognames = client.cogs.copy().keys()
	logger.info("removing cogs")
	for cogname in cognames:
		client.remove_cog(cogname)
