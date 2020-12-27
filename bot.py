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

ELTHISIONID = 123841216662994944

ALLOWEDGUILD = 747752542741725244
PREFIX = "°"

msgs = msglist.msglist(5,toTrackName)

client = discord.Client()


#EMOJIS
pepelove = "<:pepelove:778369435244429344>"
pepegun = "<:pepegun:747783377716904008>"
confusedcat = "<:confusedcat:771041402930987068>"
hm = "<:hm:779012743583498240>"
cope = "<:wojak_cope:792668283505475584>"
c_yfu = "<:code_youfuckedup:785435875030728724>"
hahaa = "<:haHaa:747783377536680066>"
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
	print("before",cmd)
	origlen = len(cmd)
	cmd = handler.find_alias(cmd)
	print("after",cmd)
	error = 0

	if(cmd == "msgarchive" and perm_valid(cmd,permlevel)):
		txt = msgs.sendable()
		if(txt.strip() == ""):
			error = 2
		else:
			error = await tryForbidden(message.channel.send, msgs.sendable())

	elif(cmd == "help" and perm_valid(cmd,permlevel)):
			cmds = handler._execComm('''SELECT cmdname,helptext,alias,permlevel from commands where enabled==1''',raw=True)
			final_cmd = []
			for c in cmds:
				if(c[3]<=permlevel):
					final_cmd.append((c[0],c[1],c[2]))
			out = ""
			for (cmdn,text,alias) in final_cmd:
				out+= f'- {cmdn} \t {text.replace("_"," ")} \t (°{alias})\n'
			error = await tryForbidden(message.channel.send,str(out))
			

	elif(cmd =="setcache" and perm_valid(cmd,permlevel)):
		try:
			newLen = int(args[1])
			newLen = msgs.set_len(newLen)
			error = await tryForbidden( message.channel.send,f"> updated cache length to {newLen}")
		except Exception:
			error = 1
	elif(cmd =="trackel"):
		toTrackID = ELTHISIONID
		toTrackName = "Aaron"
		msgs.set_user(toTrackName)
		error = await tryForbidden( message.channel.send,f'> updated tracked person')
	
	elif(cmd =="endtrack" and perm_valid(cmd,permlevel)):
		toTrackID = 0
		toTrackName = "nobody"
		msgs.set_user(toTrackName)
		error = await tryForbidden(message.channel.send, '> stopped tracking')

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

	elif(cmd == "changelog" and perm_valid(cmd,permlevel)):
		error = await tryForbidden(message.channel.send,f'> {handler.get_from_misc("changelog")}')

	elif(cmd == "setchangelog" and perm_valid(cmd,permlevel)):
		try:
			handler.set_to_misc("changelog",args[1])
			error = 0
		except:
			print("UWU SHIT GONE WRONG IN SCL HANDLING bot.py")
			error = 1

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

	elif(cmd =="addcommand" and permlevel == 4):
		handler._execComm(f'''INSERT INTO commands("cmdname","permlevel","helptext","alias","enabled") VALUES("{args[1]}",{args[2]},"{args[3]}","{args[4]}","{args[5]}")''')

	elif(cmd == "setperm" and perm_valid(cmd,permlevel)):
		res = handler.set_perm(message.mentions[0], newpermlev=args[2])
	
	elif(cmd == "triggerannoy" and perm_valid(cmd,permlevel)):
		handler.set_to_misc("annoyreaction", not handler.shouldAnnoy())
		message.channel.send(f"> Turned reaction annoyance {('Off','On')[handler.shouldAnnoy()]}")
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
		msgs.add_msg(message)
		if(handler.shouldAnnoy()): await tryForbidden( message.add_reaction,confusedcat)

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
