import discord

IMPORTS = ()


BASE_URL = "https://robohash.org/"

def get_embed(arg:str)->discord.Embed:
	embObj = discord.Embed(title="Robohash", description="RoboHash image generated from your input")
	url = BASE_URL+arg.replace(" ","%20").replace("\n","")
	embObj.set_image(url=url)
	return embObj