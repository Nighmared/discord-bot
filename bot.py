from logging import error #for discord errors
from re import split #for cmd handling
import discord # api library
import msglist # module for message tracking
import dbhandler # module for all things sqlite
import commandhandler # module for commandhandling
import uptime #module to track uptime of bot
from importlib import reload
from datetime import datetime
from sys import exit
import subprocess as sub # needed for softreload to pull from git kekw

MODULES = (
	msglist,
	dbhandler,
	commandhandler,
	uptime,
)




SUDOID = 291291715598286848
TOKEN = open(".token.txt").read()
PREFIX = "°"
STARTTIME = datetime.now()
msgs = msglist.msglist(5)
client = discord.Client()
db = dbhandler.dbhandler("discordbot.db")
time_tracker = uptime.uptime(STARTTIME)
handler = commandhandler.commandhandler(dbhandler=db,msgs=msgs,PREFIX=PREFIX,client=client,time_tracker=time_tracker)


#FIXME this is dumb, make less dumb ffs
def get_ready():
	global msgs,client,db,time_tracker,handler
	msgs = msglist.msglist(5)
	db = dbhandler.dbhandler("discordbot.db")
	time_tracker = uptime.uptime(STARTTIME)
	handler = commandhandler.commandhandler(dbhandler=db,msgs=msgs,PREFIX=PREFIX,client=client,time_tracker=time_tracker)

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

	#block bots
	if(message.author.bot and not message.author.id == handler.toTrackID):
		return
	
	isCommand = message.content.startswith(PREFIX)
	permlevel = db.get_perm_level(message.author.id)
	isJoniii = message.author.id == SUDOID #hardcode that sucker
	if(isJoniii): permlevel = 5
	cmd = db.find_alias(message.content[1:].split(" ")[0].lower())

	if(isCommand):
		log = open("log.txt","a")
		log.write(f"{message.author.name}>{message.content}\n")


	if(isCommand and cmd == ""):
		return




		
			


	if(int(db.get_from_misc("standby")) == 1  and not cmd == "deepsleep"): #ignore everything in standby
		return

	if(message.author.id == handler.toTrackID and not isCommand):
		msgs.add_msg(message)
		if(db.shouldAnnoy()): await add_reaction( message,confusedcat)

	if(isCommand):
		if not perm_valid(cmd,permlevel):
			res = 4
	#special case with softreload that only reloads the modules
		elif(cmd == "softreload" and perm_valid(cmd,permlevel)):
			sub.run(["git","pull","--no-edit"]) # git pull --no-edit
			modulenames = ""
			starttime = time_tracker.start
			for module in MODULES:
				reload(module)
				modulenames+= module.__name__ +"\n"
			
			try:
				get_ready()
				embObj = discord.Embed(title="Soft Reloading")
				embObj.add_field(name="Reloaded modules:",value=modulenames)
				res = 0
			except:
				res = 1
				embObj = discord.Embed(title="Soft Reloading",description="Aw something went wrong... Maybe try a hard reload?")
			handler.curr_msg = message
			res = max(await handler.sendMsg( channel=message.channel,toSend = embObj),res)

		else:
			res = await handler.commandHandler(message,permlevel)
		if(res == 99): #RELOAD
			exit(0)
		await add_reaction( message,db.get_emote(res))
		await message.delete(delay=3)
		
client.run(TOKEN)
