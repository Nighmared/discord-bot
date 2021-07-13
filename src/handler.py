import logging
from re import split #for cmd handling
import discord
from discord.errors import Forbidden # api library
import msglist # module for message tracking
import dbhandler # module for all things sqlite
import commandhandler # module for commandhandling
import uptime #module to track uptime of bot
from importlib import reload
import subprocess as sub # needed for softreload to pull from git kekw
from time import sleep
import sys
import botlogger 
import loophandler as loop

IMPORTS = (botlogger, msglist, dbhandler, commandhandler, uptime,loop)

SUDOID = 291291715598286848 

logger = logging.getLogger("botlogger")

ISRELOADING = True
PREFIX = "°" #default value for initialization


cmdhandler = time_tracker = msgs = db = None
def init(client:discord.Client,STARTTIME):
	global cmdhandler,time_tracker,msgs,db, PREFIX
	time_tracker = uptime.uptime(STARTTIME)
	msgs = msglist.msglist(5)
	try:
		db = dbhandler.Dbhandler("discordbot.db")
		dbPREFIX = db.get_from_misc('prefix')
		if dbPREFIX:
			PREFIX = dbPREFIX
		else:
			PREFIX = "°" #fallback :>

		if int(db.get_from_misc("debug"))>0:
			print("DEBUGGING MODE. PREFIX IS: ",PREFIX)

	except Exception as e:
		print(e)
		PREFIX = "&"


	
		
	cmdhandler = commandhandler.commandhandler(dbhandler=db,msgs=msgs,PREFIX=PREFIX,client=client,time_tracker=time_tracker) 
	botlogger.get_ready()


this_emote = "<:this:747783377662378004>"

def perm_valid(cmd:str,permlevel:int) -> bool:
	return permlevel>= db.get_cmd_perm(cmd)



async def add_reaction(message, emote):
	try:
		await message.add_reaction(emote)
		return 0
	except discord.errors.Forbidden:
		return 5
	except discord.errors.HTTPException as e:
		logger.warning("Couldn't add emote as reaction:"+emote)
		print(e)
		return 1


#FIXME this is dumb, make less dumb ffs -> give all classes "backup" and "restore" methods so it can be just iterating over stuff
def get_ready(client:discord.Client, STARTTIME):
	global msgs,db,time_tracker,cmdhandler,PREFIX
	msgs = msglist.msglist(5)
	db = dbhandler.Dbhandler("discordbot.db")
	PREFIX = db.get_from_misc("prefix")
	time_tracker = uptime.uptime(STARTTIME)
	cmdhandler = commandhandler.commandhandler(dbhandler=db,msgs=msgs,PREFIX=PREFIX,client=client,time_tracker=time_tracker)
	last_msgs_backup = cmdhandler.last_MSG
	cmdhandler.last_MSG = last_msgs_backup
	botlogger.get_ready()
	



async def doreload(message:discord.Message,client:discord.Client,STARTTIME,msgs_backup): #reloads all dependencies
	global ISRELOADING
	
	work_to_do = True
	backoff = 10
	is_recovering = False
	
	reload(discord)
	loop.discard(client)


	while work_to_do:	
		failedmodules = ""
		modulenames = "discord.py\nhandler.py\n"
		submodules = set()
		for module in IMPORTS:
			try:
				reload(module)
			except ModuleNotFoundError as e:
				failedmodules+=module.__name__+"\n"
				failedmodules+="⤷"+str(e).split("'")[1]+"\n"
				continue
			modulenames+= module.__name__ +"\n"
			try:
				module.IMPORTS
			except AttributeError:
				logger.error(f"{module.__name__} missing IMPORTS list")
				continue;
			for subimport in module.IMPORTS:
				if subimport not in submodules:
					submodules.add(subimport)
					modulenames+= "⤷"+subimport.__name__+"\n"
					for subsub in subimport.IMPORTS:
						if(subsub not in submodules and subsub not in IMPORTS):
							submodules.add(subsub)
							modulenames += "➥  "+subsub.__name__+"\n"
		
		for submodule in submodules:
			try:
				reload(submodule)
			except ModuleNotFoundError as e:
				failedmodules+="➥"+str(e).split("'")[1]+"\n"
				continue

		embObj = discord.Embed(title="Soft Reloading")
		embObj.add_field(name="✅ Reloaded modules:",value=modulenames)
		embObj.set_author(name=message.author.name,icon_url=message.author.avatar_url)
		embObj.timestamp = uptime.get_now_utc()

		if is_recovering: # if already retrying
			await msgs_backup.pop().delete() #dont clutter

		if len(failedmodules.strip())>0 : #this applies when anything failed during reloading
			embObj.add_field(name="❌ Couldn't import:",value=failedmodules)
			embObj.add_field(name="BackOff-Retry",value=f"Will retry loading in {backoff} seconds")

			is_recovering = True
		
			sent_msg = await message.channel.send(embed=embObj)
			msgs_backup.append(sent_msg) # keep the message list up to date until it gets put to cmdhandler again
			
			sleep(backoff) #wait until next reload
			backoff*= 2 #exponential backoff
			
			sub.run(["git","pull","--no-edit"]) # git pull --no-edit -> get newest changes from github
		else:
			work_to_do = False
	
	if(backoff>512): #give up at some point
		logger.fatal("gave up on reloading after trying multiple times.. something really doesnt work here")
		sys.exit(1) # give up with nonzero error code
			
	#at this point everything should be fine
	get_ready(client=client,STARTTIME = STARTTIME)
	res = 0
	cmdhandler.last_MSG = msgs_backup
	cmdhandler.curr_msg = message

	logger.info("Return from softreload")
	if type(message.channel) is discord.channel.DMChannel or message.author.nick is None:
		callee = message.author.name
	else:
		callee = message.author.nick
	

	res = max(await cmdhandler.sendMsg( channel=message.channel,toSend = embObj,callee=callee, callee_pic = message.author.avatar_url ),res)
	await add_reaction(message,db.get_emote(res))
	ISRELOADING = False
	if isinstance(message.channel,discord.TextChannel):
		try:
			await message.delete()
		except Forbidden:
			None #cant do anyting :shrug:


async def do_the_thing(channel:discord.TextChannel,name:str, id:int, avatar_url:str):
	global PREFIX
	embObj = discord.Embed(title="How did this happen? :O")
	f = discord.File(cmdhandler.dbhandler.get_nhentai_path_by_id(id)[0].rstrip(".blurred.jpg")+".jpg","IMG.jpg", spoiler=True)
	embObj.set_image(url="attachment://IMG.jpg")
	await cmdhandler.sendMsg(channel,embObj,callee=name,file=f, callee_pic = avatar_url )

async def handle(message:discord.Message) -> int:
	global ISRELOADING
	global PREFIX
	if ISRELOADING: return 0# prevent errors during reloading
	#block bots
	if(message.author.bot and not message.author.id == cmdhandler.toTrackID):
		return 0
	
	#count messages per user
	db.increment_user_message_count(message.author.id, message.author.name,message.author.mention)
	

	if message.guild and message.guild.id in (747752542741725244,695246759382745108) and message.content.startswith("$g") and len(args := message.content.split(" "))>1 and args[1].isnumeric():
		db.add_average(message.author.id, int(args[1]))


	isCommand = message.content.startswith(PREFIX)
	permlevel = db.get_perm_level(message.author.id)
	isJoniii = message.author.id == SUDOID #hardcode that sucker
	if(isJoniii): permlevel = 10
	cmd = db.find_alias(message.content[1:].split(" ")[0].lower())


	if(int(db.get_from_misc("standby")) == 1  and not cmd == "deepsleep"): #ignore everything in standby
		return

	#easteregg lel
	if "177013" in message.content.strip().replace(" ","") and not isCommand:
		await do_the_thing(message.channel, message.author.nick, 177013,message.author.avatar_url)
	if(isCommand):
		logger.info(f"{message.author.name}>{message.content}")


	if(message.author.id == cmdhandler.toTrackID and not isCommand):
		msgs.add_msg(message)
		if(db.shouldAnnoy()): await add_reaction( message,this_emote)

	if(isCommand and cmd): #prevent handling invalid commands; find_alias returns "" on unknown commands and bool("") is False :>
		
		if cmd =="" or not perm_valid(cmd,permlevel): #!!! perms already checked heree
			res = 4

	#special case with softreload that only reloads the modules
		elif(cmd == "softreload" and perm_valid(cmd,permlevel)):
			ISRELOADING = True
			db.close_down()
			return 88

		else:
			res = await cmdhandler.commandHandler(message,permlevel)
		if(res == 99): #RELOAD
			db.close_down()
			return 99
		elif res == 77: #update prefix
			PREFIX = db.get_from_misc("prefix")
			res = 0 # set to normal reaction
		await add_reaction( message,db.get_emote(res))
		if isinstance(message.channel, discord.TextChannel):
			await message.delete(delay=3)
