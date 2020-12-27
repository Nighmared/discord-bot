from logging import error
from re import split
import discord
import msglist
import dbhandler
import issues
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


reaction_text_dict = {
	0:"Everything gud",
	1:"nono thats not how its supposed to go",
	2:"Nothing to display",
	3:"You fucked up ur command mister",
	4:"Not enough permissions",
	5:"All fine but bot can't text here... F",
}



def perm_valid(cmd:str,permlevel:int) -> bool:
	return permlevel>= handler.get_cmd_perm(cmd)


async def sendMsg(channel,toSend):
	print(type(toSend))
	try:
		if(type(toSend) == discord.embeds.Embed):
			await channel.send(embed=toSend)
		else:
			embVar = discord.Embed(title="GOTTA FIX THIS CMD", description=toSend,color=0xff0000)
			await channel.send(embed = embVar)
		return 0
	except discord.errors.Forbidden:
		return 5

async def add_reaction(message, emote):
	try:
		await message.add_reaction(emote)
		return 0
	except discord.errors.Forbidden:
		return 5

#TODO: DB for admins, current tracker etc !!
async def commandHandler(message:discord.message,permlevel:int) -> int:
	global toTrackID
	global toTrackName
	args = message.content[1:].split(" ")
	cmd = args[0]
	origlen = len(cmd)
	cmd = handler.find_alias(cmd)
	if not handler.cmd_is_enabled(cmd):
		error = 4
		print(f"disabled cmd: {cmd}")
		return error
	error = 0

	if(cmd == "msgarchive" and perm_valid(cmd,permlevel)):
		msgls = msgs.sendable()
		if(len(msgls)== ""):
			error = 2
		else:
			embObj = discord.Embed(title="Tracker",description=f"Recent messages by {msgls[0].author.nick}")
			fieldStr = ""
			for msg in msgls:
				fieldStr+=f"{str(msg.created_at)[:-4]} {msg.author.nick}-> {msg.channel.name}: {msg.content[:100]}\n"
			embObj.add_field(name="Messagehistory",value=fieldStr,inline=True)

			error = await sendMsg(message.channel, embObj)

	elif(cmd == "help" and perm_valid(cmd,permlevel)):
			cmds = handler._execComm('''SELECT cmdname,helptext,alias,permlevel from commands where enabled==1''',raw=True)
			final_cmd = []
			for c in cmds:
				if(c[3]<=permlevel):
					final_cmd.append((c[0],c[1],c[2]))
			embObj = discord.Embed(title="Help", description="Displaying all available commands depending on callees permissionlevel",color=0x00f0f0)
			for (cmdn,text,alias) in final_cmd:
				embObj.add_field(name=f'`{PREFIX}{cmdn}` (`{PREFIX}{alias}`)',value =f'{text.replace("_"," ")}',inline=True)
			error = await sendMsg(message.channel,embObj)

	elif(cmd =="setversion" and perm_valid(cmd,permlevel)):
		try:
			handler.set_to_misc("version",args[1])
			error = 0
		except:
			error = 1	
	
	elif(cmd == "showissues" and perm_valid(cmd,permlevel)):
		res = handler._execComm("select * from issues",True)
		embObj = discord.Embed(title="Issues",color=0xff0f00)
		for id,title in res:
			embObj.add_field(name=id,value=title,inline=False)
		error = await sendMsg(message.channel,embObj)

	elif(cmd == "reloadissues" and perm_valid(cmd,permlevel)):
		ls = issues.getIssues()
		if ls[0][0] == -1:
			error = 1
		else:
			for issue in ls:
				handler.addIssue(issue)
			
			error = await sendMsg(message.channel,"issues reloaded")


	elif(cmd =="setcache" and perm_valid(cmd,permlevel)):
		try:
			newLen = int(args[1])
			newLen = msgs.set_len(newLen)
			error = await sendMsg( message.channel,f" updated cache length to {newLen}")
		except Exception:
			error = 1
	elif(cmd =="trackel"):
		toTrackID = ELTHISIONID
		toTrackName = "Aaron"
		msgs.set_user(toTrackName)
		error = await sendMsg( message.channel,f' updated tracked person')
	
	elif(cmd =="endtrack" and perm_valid(cmd,permlevel)):
		toTrackID = 0
		toTrackName = "nobody"
		msgs.set_user(toTrackName)
		error = await sendMsg(message.channel, ' stopped tracking')

	elif(cmd == "settrack" and perm_valid(cmd,permlevel)):
		try:
			user = message.mentions[0]
			toTrackID = user.id
			toTrackName = user.nick
			msgs.set_user(toTrackName)
			error = await sendMsg( message.channel,f" updated tracked user to {toTrackName}")
		except IndexError:
			error = 3
		except Exception:
			error = 1

	elif(cmd == "gettrack" and perm_valid(cmd,permlevel)):
		error = await sendMsg( message.channel,f" currently tracking {toTrackName}")

	elif(cmd == "changelog" and perm_valid(cmd,permlevel)):
		error = await sendMsg(message.channel,f' {handler.get_from_misc("changelog")}')

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
		error = await sendMsg( message.channel.send,f" {resttxt}")

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
			await sendMsg(message.channel,res)
	
	elif(cmd == "reload" and perm_valid(cmd,permlevel)):
		embObj = discord.Embed(title="Reloading...",description="let's hope this doesn't fuck anything up...",color=0x00ff00)
		await sendMsg(message.channel,embObj)
		return 99

	elif(cmd =="addcommand" and permlevel == 4):
		handler._execComm(f'''INSERT INTO commands("cmdname","permlevel","helptext","alias","enabled") VALUES("{args[1]}",{args[2]},"{args[3]}","{args[4]}","{args[5]}")''')

	elif(cmd == "setperm" and perm_valid(cmd,permlevel)):
		res = handler.set_perm(message.mentions[0], newpermlev=args[2])
	
	elif(cmd == "triggerannoy" and perm_valid(cmd,permlevel)):
		handler.set_to_misc("annoyreaction", (not handler.shouldAnnoy()))
		await sendMsg(message.channel,f" Turned reaction annoyance {('Off','On')[handler.shouldAnnoy()]}")
	
	elif(cmd == "togglecmd" and perm_valid(cmd,permlevel)):
		totogglecmd = ""
		try:
			totogglecmd = args[1]
			handler._execComm(f'''UPDATE commands SET enabled={(1,0)[handler.cmd_is_enabled(totogglecmd)]} WHERE cmdname=="{totogglecmd}"''')
		except IndexError:
			error = 3
		except:
			error = 2
	
	elif(cmd == "fixissue" and perm_valid(cmd,permlevel)):
		try:
			arg = args[1]
			handler.fixissue(arg)
		except IndexError:
			error = 3
		except:
			error = 2
	
	elif(cmd == "testembed" and perm_valid(cmd,permlevel)):
		emb = discord.Embed(title="title",description="descr",color=0x00ff00)
		emb.add_field(name="test1",value="val1",inline=False)
		emb.add_field(name="test2", value="val2", inline = True)
		await sendMsg(message.channel,emb)
	else:
		error = 1
		if(not perm_valid(cmd,permlevel)):
			error = 4
	return error

@client.event
async def on_ready():
	print(f'{client.user} has connected')

@client.event
async def on_message(message:discord.message):
	global addedEmotesToHelp

	#block bots
	if(message.author.bot):
		return

	#allow only one server
#	if(message.guild.id != ALLOWEDGUILD):return
	
	isCommand = message.content.startswith(PREFIX)
	permlevel = handler.get_perm_level(message.author.id)
	isJoniii = message.author.id == SUDOID # for super cmds
	if(isJoniii): permlevel = 4
	cmd = handler.find_alias(message.content[1:].split(" ")[0])


	error_dict = {
		0 : pepelove, #success
		1 : pepegun, #invalid stuff
		2 : hm, # no msgs to display
		3 : c_yfu, # wrong args
		4 : cope, #perms
		5 : hahaa, #bot cant send here D;
	}



	if(message.author.id == toTrackID and not isCommand):
		#print(message.content)
		msgs.add_msg(message)
		if(handler.shouldAnnoy()): await add_reaction( message,confusedcat)

	if(isCommand):
		if not perm_valid(cmd,permlevel):
			print("a")
			res = 4
		else:
			res = await commandHandler(message,permlevel)
		if(res == 99): #RELOAD
			exit(0)
		await add_reaction( message,error_dict[res])
		
		

client.run(TOKEN)
