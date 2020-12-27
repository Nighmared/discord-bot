from logging import error
from re import split
import discord
import msglist
import dbhandler
from sys import exit



TOKEN = open(".token.txt").read()

SUDOID = 291291715598286848
toTrackID = 0
toTrackName = "nobody"

ALLOWEDGUILD = 747752542741725244
PREFIX = "°"

msgs = msglist.msglist(5,toTrackName)

client = discord.Client()


#EMOJIS
pepelove = client.get_emoji(792668124322201610)
pepegun = client.get_emoji(792668155616952320)
confusedcat = client.get_emoji(792668214185164811)
hm = client.get_emoji(792668245973925919)
cope = client.get_emoji(792668283505475584)
c_yfu = client.get_emoji(792668458281730059)
hahaa = client.get_emoji(747783377536680066)
########



handler = dbhandler.dbhandler("discordbot.db")

help_string = f'''

	**Commands** of *gotta go brr*:
	- {PREFIX}help \t shows this message
	- {PREFIX}msgarchive (ma) \t shows recent msgs of currently tracked user
	- {PREFIX}changelog (cl) \t show changes made in latest update
	- {PREFIX}info (i) \t shows some info abt bot
	- ??

**Reaction**:
'''

addedEmotesToHelp = False

help_super=f''' **ADMIN Commands**
	- {PREFIX}settrack (st) \t sets which user to track
	- {PREFIX}setcache (sc) \t sets how many msgs are cached
	- {PREFIX}gettrack (gt) \t show currently tracked user
	- {PREFIX}say \t say something
	- {PREFIX}setstatus (ss) \t sets activity of bot
	- {PREFIX}reload (rl) \t restarts bot and pulls fresh copy
	
	**Exclusive joniii commands**
	- {PREFIX}setchangelog (scl) \t updates what changelog command returns
	- {PREFIX}setversion (sv) \t set version
	- {PREFIX}setperm (mp) \t allow or deny some command for some user
	- {PREFIX}ac <cmdname> <permlevel> <help_text> <alias> <enabled = 0/1>
	

'''

CMD_aliases = {
	"st":"settrack",
	"sc":"setcache",
	"gt":"gettrack",
	"ma":"msgarchive",
	"i":"info",
	"cl":"changelog",
	"ss":"setstatus",
	"?":"help",
	"rl":"reload",
	"scl":"setchangelog",
	"sv":"setversion",
	"mp":"setperm",
	"esql":"execsql",
}

reaction_text_dict = {
	0:"Everything gud",
	1:"nono thats not how its supposed to go",
	2:"Nothing to display",
	3:"You fucked up ur command mister",
	4:"Not enough permissions",
	5:"All fine but bot can't text here... F",
}


cmd_help_dict = {
	"setstatus":'''
	> sets status
	`°setstatus "newstatus" [type]`
	types:
	 1 -> playing <status>
	 2 -> listening to <status>
	 3 -> watching <status>
	 4 -> 
	 5 -> competing in <status>'''
}
admin_cmds = ("setstatus","setcache","gettrack","say","settrack","reload")


def perm_valid(cmd:str,permlevel:int) -> bool:
	return permlevel>= handler.get_cmd_perm(cmd)


async def superHandler(message:discord.message,cmd:str)->int:
	return await tryForbidden(message.channel.send,f"{cmd} is WIP")

async def tryForbidden(func,arg):
	try:
		await func(arg)
		return 0
	except discord.errors.Forbidden:
		#print("forbidden uwu")
		return 50

#TODO: DB for admins, current tracker etc !!
async def commandHandler(message:discord.message,permlevel:int) -> int:
	global toTrackID
	global toTrackName
	args = message.content[1:].split(" ")
	cmd = args[0]
	origlen = len(cmd)
	if(cmd in CMD_aliases.keys()):
		cmd = CMD_aliases[cmd]
	error = 0

	if(cmd == "msgarchive" and perm_valid(cmd,permlevel)):
		txt = msgs.sendable()
		if(txt.strip() == ""):
			error = 2
		else:
			error = await tryForbidden(message.channel.send, msgs.sendable())

	elif(cmd == "help" and perm_valid(cmd,permlevel)):
			if(len(args)>1):
				if(args[1] in cmd_help_dict.keys()):
					error = await tryForbidden(message.channel.send,cmd_help_dict[args[1]])
			else:
				txt = help_string
				if(permlevel>=1):
					txt += help_super
				error = await tryForbidden(message.channel.send,txt)

	elif(cmd =="setcache" and perm_valid(cmd,permlevel)):
		try:
			newLen = int(args[1])
			newLen = msgs.set_len(newLen)
			error = await tryForbidden( message.channel.send,f"> updated cache length to {newLen}")
		except Exception:
			error = 1
	
	elif(cmd == "settrack" and perm_valid(cmd,permlevel)):
		try:
			user = message.mentions[0]
			toTrackID = user.id
			toTrackName = user.nick
			msgs.set_user(toTrackName)
			error = await tryForbidden( message.channel.send,f"> updated tracked user to {toTrackName}")
		except IndexError:
			error = 3
		except Exception:
			error = 1

	elif(cmd == "gettrack" and perm_valid(cmd,permlevel)):
		error = await tryForbidden( message.channel.send,f"> currently tracking {toTrackName}")

	elif(cmd == "say" and perm_valid(cmd,permlevel)):
		resttxt = ""
		for a in args[1:]:
			resttxt += " "+a
		error = await tryForbidden( message.channel.send,f"> {resttxt}")

	elif (cmd == "setstatus" and perm_valid(cmd,permlevel)):
		type = 1
		splitbyquot = message.content.split("\"")
		if(len(splitbyquot) not in (2,3)):
			if len(args)<2:
				return 3 #u fucked up
			else:
				stringarg = args[1]
			if(len(args)>2 and args[2].isnumeric()):
				type = args[2]
		else:
			stringarg = splitbyquot[1]
			if(len(splitbyquot)==3 and splitbyquot[2].isnumeric()):
				type = int(splitbyquot[2])
		await client.change_presence(activity=discord.Activity(name=stringarg,type= type))
	elif (cmd =="execsql" and perm_valid(cmd,permlevel)):
		res = handler._execComm(message.content[(origlen+1):].strip())
		if(res !=-10):
			await tryForbidden(message.channel.send,res)
	
	elif(cmd == "reload" and perm_valid(cmd,permlevel)):
		await tryForbidden( message.channel.send,"> reloading ... [lets hope this goes fine]")
		return 99

	elif(cmd =="ac" and permlevel == 4):
		handler._execComm(f'''INSERT INTO commands("cmdname","permlevel","helptext","alias","enabled") VALUES("{args[1]}",{args[2]},"{args[3]}","{args[4]}","{args[5]})''')

	elif(cmd == "setperm" and perm_valid(cmd,permlevel)):
		res = handler.set_perm(message.mentions[0], newpermlev=args[2])
	else:
		error = 1
		if(not perm_valid(cmd,permlevel)):
			error = 4
	return error


def getEmoji(guild,name):
	return discord.utils.get(guild.emojis,name=name)


@client.event
async def on_ready():
	print(f'{client.user} has connected')

@client.event
async def on_message(message:discord.message):
	global addedEmotesToHelp
	global help_string

	#block bots
	if(message.author.bot):
		return

	#allow only one server
#	if(message.guild.id != ALLOWEDGUILD):return

	guild = message.guild
	
	isCommand = message.content.startswith(PREFIX)
	permlevel = handler.get_perm_level(message.author.id)
	isJoniii = message.author.id == SUDOID # for super cmds
	if(isJoniii): permlevel = 4
	cmd = message.content[1:].split(" ")[0]
	if cmd in CMD_aliases.keys(): cmd = CMD_aliases[cmd]


	error_dict = {
		0 : pepelove, #success
		1 : pepegun, #invalid stuff
		2 : hm, # no msgs to display
		3 : c_yfu, # wrong args
		4 : cope, #perms
		5 : hahaa, #bot cant send here D;
	}

	if not addedEmotesToHelp:
		addedEmotesToHelp = True
		for key in error_dict.keys():
			help_string+=f"{error_dict[key]}\t{reaction_text_dict[key]}\n"



	if(message.author.id == toTrackID and not isCommand):
		#print(message.content)
		await tryForbidden( message.add_reaction,confusedcat)
		msgs.add_msg(message)

	if(isCommand):
		if not perm_valid(cmd,permlevel):
			print("a")
			res = 4
		else:
			res = await commandHandler(message,permlevel)
		if(res == 99): #RELOAD
			exit(0)
		await tryForbidden( message.add_reaction,error_dict[res])
		
		

client.run(TOKEN)
