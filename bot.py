from logging import error
from re import split
import discord
import msglist
from sys import exit


TOKEN = open(".token.txt").read()
ADMINS = (
	291291715598286848,
)
toTrackID = 0
toTrackName = "nobody"

ALLOWEDGUILD = 747752542741725244
PREFIX = "°"

msgs = msglist.msglist(5,toTrackName)

client = discord.Client()



help_string = f'''

	**Commands** of *gotta go brr*:
	- {PREFIX}help \t shows this message
	- {PREFIX}msgarchive (ma) \t shows recent msgs of currently tracked user
	- ??

**Reaction**:
'''

addedEmotesToHelp = False

help_admin=f''' **ADMIN Commands**
	- {PREFIX}settrack (st) \t sets which user to track
	- {PREFIX}setcache (sc) \t sets how many msgs are cached
	- {PREFIX}gettrack (gt) \t show currently tracked user
	- {PREFIX}say \t say something
	- {PREFIX}setstatus (ss) \t sets activity of bot
	- {PREFIX}reload (rl) \t restarts bot and pulls fresh copy
	

'''

CMD_aliases = {
	"st":"settrack",
	"sc":"setcache",
	"gt":"gettrack",
	"ma":"msgarchive",
	"ss":"setstatus",
	"?":"help",
	"rl":"reload",
}

reaction_text_dict = {
	0:"Everything gud",
	1:"nono thats not how its supposed to go",
	2:"Nothing to display",
	3:"You fucked up ur command mister",
	4:"Not enough permissions"
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
admin_cmds = ("setstatus","setcache","gettrack","say","settrack")


#TODO: DB for admins, current tracker etc !!
async def commandHandler(message:discord.message,isAdmin:bool) -> int:
	global toTrackID
	global toTrackName
	args = message.content[1:].split(" ")
	cmd = args[0]

	if(cmd in CMD_aliases.keys()):
		cmd = CMD_aliases[cmd]
	error = 0

	if(cmd == "msgarchive"):
		txt = msgs.sendable()
		if(txt.strip() == ""):
			error = 2
		else:
			try:
				await message.channel.send(msgs.sendable())
			except discord.errors.Forbidden:
				error = 5

	elif(cmd == "help"):
		try:
			if(len(args)>1):
				if(args[1] in cmd_help_dict.keys() and isAdmin or not (args[1] in admin_cmds)):
					await message.channel.send(cmd_help_dict[args[1]])
			else:
				txt = help_string
				if(isAdmin):
					txt += help_admin
				await message.channel.send(txt)
		except discord.errors.Forbidden:
			error = 5

	elif(isAdmin and cmd =="setcache"):
		try:
			newLen = int(args[1])
			newLen = msgs.set_len(newLen)
			await message.channel.send(f"> updated cache length to {newLen}")
		except discord.errors.Forbidden:
			error = 5
		except Exception:
			error = 1
	
	elif(isAdmin and cmd == "settrack"):
		try:
			user = message.mentions[0]
			toTrackID = user.id
			toTrackName = user.nick
			msgs.set_user(toTrackName)
			await message.channel.send(f"> updated tracked user to {toTrackName}")

		except IndexError:
			error = 3
		except discord.errors.Forbidden:
			error = 5
		except Exception:
			error = 1

	elif(isAdmin and cmd == "gettrack"):
		try:
			await message.channel.send(f"> currently tracking {toTrackName}")
		except discord.errors.Forbidden:
			error = 5
	elif(isAdmin and cmd == "say"):
		resttxt = ""
		for a in args[1:]:
			resttxt += " "+a
		try:
			await message.channel.send(f"> {resttxt}")
		except discord.errors.Forbidden:
			error = 5

	elif (isAdmin and cmd == "setstatus"):
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
	elif(isAdmin and cmd == "reload"):
		try:
			await message.channel.send("> reloading ... [lets hope this goes fine]")
		except discord.errors.Forbidden:
			print("<couldnt send confirmation in channel but reload anyway>")
		return 99
	else:
		error = 1
		if(cmd in admin_cmds):
			error = 4
		if(cmd == "help" and len(args)>1 and args[1] in admin_cmds):
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
	if(message.guild.id != ALLOWEDGUILD):
		return

	guild = message.guild
	pepelove = getEmoji(guild,"pepelove")
	pepegun = getEmoji(guild,"pepegun")
	confusedcat = getEmoji(guild,"confusedcat")
	hm = getEmoji(guild,"hm")
	cope = getEmoji(guild,"wojak_cope")
	c_yfu = getEmoji(guild,"code_youfuckedup")
	hahaa = getEmoji(guild,"haHaa")
	isCommand = message.content.startswith(PREFIX)
	isAdmin = message.author.id in ADMINS
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
		print(message.content)
		await message.add_reaction(confusedcat)
		msgs.add_msg(message)

	if(isCommand):
		if(cmd in admin_cmds and not isAdmin):
			await message.add_reaction(error_dict[4])
			return
		res = await commandHandler(message,isAdmin)
		if(res == 99): #RELOAD
			exit(0)
		await message.add_reaction(error_dict[res])
		
		

client.run(TOKEN)
