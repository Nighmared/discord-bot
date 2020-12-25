import discord

TOKEN = open(".token.txt").read()


client = discord.Client()

@client.event
	async def on_ready():print(f'{client.user} has connected')


client.run(TOKEN)