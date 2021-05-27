
import discord
import asyncio
import threading
import sys
TOKENF = open(".token.txt")
TOKEN = TOKENF.read()
TOKENF.close()
client = discord.Client()
curr_channel = None

@client.event
async def on_ready():
	global curr_server
	curr_server = client.get_guild(747752542741725244)
	print(curr_server)
	sys.stdin.flush()


@client.event
async def on_message(message:discord.message):
	if message.channel != curr_channel: # or message.author.bot:
		return
	start = f"[{message.channel.name}] {message.author.name}"
	print(f"\n{start.ljust(40)}>{message.content}")


def inhandler():
	global curr_channel
	msg = str(sys.stdin.readline())
	if msg.startswith("-"):
		cmd = msg[1:].split(" ")[0].strip()
		if(cmd == "channels"):
			indx = 0
			for chan in curr_server.channels:
				print(indx,chan)
				indx+=1
		elif(cmd == "setchannel"):
			indx = int(msg[1:].split(" ")[1])
			curr_channel = curr_server.channels[indx]
			print(">> set channel to ",curr_channel," <<")
	else:
		if curr_channel != None:
			fut = asyncio.get_running_loop().create_task(curr_channel.send(msg))


asyncio.get_event_loop().add_reader(sys.stdin,inhandler)

client.run(TOKEN)

#print(client.guilds)
