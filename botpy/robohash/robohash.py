import logging

import discord

IMPORTS = ()
logger = logging.getLogger("botlogger")


BASE_URL = "https://robohash.org/"


def get_embed(arg: str) -> discord.Embed:
    embObj = discord.Embed(
        title="Robohash", description="RoboHash image generated from your input"
    )
    formatted = arg.replace(" ", "%20").replace("\n", "")
    url = BASE_URL + formatted
    embObj.set_image(url=url)
    field_value = formatted if len(formatted) < 1024 else formatted[:1019] + "[...]"
    embObj.add_field(name="Input", value=field_value)
    return embObj
