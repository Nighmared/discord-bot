from logging import error
from re import split
import discord
import msglist
import dbhandler
import commandhandler
from sys import exit


SUDOID = 291291715598286848
TOKEN = open(".token.txt").read()
PREFIX = "°"
msgs = msglist.msglist(5)
client = discord.Client()
db = dbhandler.dbhandler("discordbot.db")
handler = commandhandler.commandhandler(dbhandler=db,msgs=msgs,PREFIX=PREFIX,client=client)



#EMOJIS
pepelove = "<:pepelove:778369435244429344>"
pepegun = "<:pepegun:747783377716904008>"
confusedcat = "<:confusedcat:771041402930987068>"
hm = "<:hm:779012743583498240>"
cope = "<:wojak_cope:767839352255676417>"
c_yfu = "<:code_youfuckedup:785435875030728724>"
hahaa = "<:haHaa:747783377536680066>"
########





def perm_valid(cmd:str,permlevel:int) -> bool:
	return permlevel>= db.get_cmd_perm(cmd)



async def add_reaction(message, emote):
	try:
		await message.add_reaction(emote)
		return 0
	except discord.errors.Forbidden:
		return 5

@client.event
async def on_ready():
	print(f'{client.user} has connected')

@client.event
async def on_message(message:discord.message):

	#block bots and elthision
	if(message.author.bot):
		return
	
	isCommand = message.content.startswith(PREFIX)
	permlevel = db.get_perm_level(message.author.id)
	isJoniii = message.author.id == SUDOID #hardcode that sucker
	if(isJoniii): permlevel = 5
	cmd = db.find_alias(message.content[1:].split(" ")[0].lower())

	if(isCommand or message.author.id == 123841216662994944):
		log = open("log.txt","a")
		log.write(f"{message.author.name}>{message.content}\n")
		#if(message.author.id == 123841216662994944):
		#	return



	if(cmd == ""):
		return


	


	if(int(db.get_from_misc("standby")) == 1  and not cmd == "deepsleep"): #ignore everything in standby
		return

	if(message.author.id == handler.toTrackID and not isCommand):
		#print(message.content)
		msgs.add_msg(message)
		if(db.shouldAnnoy()): await add_reaction( message,confusedcat)

	if(isCommand):
		if not perm_valid(cmd,permlevel):
			res = 4
		else:
			res = await handler.commandHandler(message,permlevel)
		if(res == 99): #RELOAD
			exit(0)
		await add_reaction( message,db.get_emote(res))
		await message.delete(delay=3)
		
client.run(TOKEN)
