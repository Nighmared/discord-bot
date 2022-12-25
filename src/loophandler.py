import logging
import discord
import discord.ext.commands

import handler
import loops.guesscleaner as guesscleaner
import loops.polyring as polyring

IMPORTS = (polyring, guesscleaner)
logger = logging.getLogger("botlogger")


async def init(client: discord.ext.commands.Bot, handler_ref: handler):  # type: ignore
    LOOPCOGS = (
        polyring.PolyringFetcher,
        guesscleaner.GuessCleaner,
    )

    logger.info("adding cogs")
    for cog in LOOPCOGS:
        await client.add_cog(cog(client, handler_ref))


async def discard(client: discord.ext.commands.Bot):
    cognames = client.cogs.copy().keys()
    logger.info("removing cogs")
    for cogname in cognames:
        await client.remove_cog(cogname)
