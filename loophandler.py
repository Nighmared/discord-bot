import discord
import discord.ext.commands
import logging
import loops.polyring as polyring
import handler

IMPORTS = (polyring,)
logger = logging.getLogger("botlogger")

LOOPCOGS = (
	polyring.PolyringFetcher,
)

def init(client: discord.ext.commands.Bot,handler_ref:handler):
	for cog in LOOPCOGS:
		client.add_cog(cog(client,handler_ref))


def discard(client:discord.ext.commands.Bot):
	cognames = client.cogs.copy().keys()
	for cogname in cognames:
		client.remove_cog(cogname)
