from discord import colour
from discord.embeds import Embed
import importlib
import dbhandler
import discord
import issues
import msglist
import neko

IMPORTS = (neko,issues)



class commandhandler:
	ISSUECOLOR = 0x00f0f0 #lightblue
	TRACKERCOLOR = 0x660066 #pinkish
	SYSTEMCOLOR = 0x009900# green
	QUERYCOLOR = 0xffcc00 # yellow
	NEKOCOLOR = 0xcc6699
	EMBEDSIZELIMIT = 1024
	MAXNUMBEROFEMBEDS = 25



	def __init__(self,
	dbhandler:dbhandler.dbhandler,
	msgs:msglist,
	PREFIX:str,
	time_tracker,
	client,
	):
		self.msgs = msgs
		self.dbhandler = dbhandler
		self.toTrackID = 0
		self.toTrackName = "nobody"
		self.toTrackUser = None
		self.last_MSG = []
		self.PREFIX = PREFIX
		self.client = client
		self.uptime_tracker = time_tracker


	def perm_valid(self,cmd:str,permlevel:int)->bool:
		return permlevel >= self.dbhandler.get_cmd_perm(cmd)
	
	async def sendMsg(self,channel,toSend):
		if(type(toSend) == discord.embeds.Embed):
			toSend.set_footer(text=f"Answering to {self.curr_msg.author.name}")
			self.last_MSG.append(await channel.send(embed=toSend))
		else: #only the case for say command
			self.last_MSG.append(await channel.send(str(toSend)))
		return 0
	



	async def commandHandler(self,message:discord.message,permlevel:int) -> int:
		self.curr_msg = message
		args = message.content[1:].split(" ")
		cmd = args[0].lower()
		origlen = len(cmd)
		cmd = self.dbhandler.find_alias(cmd)
		if(cmd == ""):
			return 3
		if not self.dbhandler.cmd_is_enabled(cmd):
			error = 4
			print(f"[commandhandler.py] disabled/invalid cmd: {cmd}")
			return error
		error = 0


		if(cmd == "msgarchive" and self.perm_valid(cmd,permlevel)):
			error = await self.msgarchive(message.channel)

		elif(cmd == "help" and self.perm_valid(cmd,permlevel)):
			error = await self.help(message.channel,permlevel)
			
		elif(cmd =="setversion" and self.perm_valid(cmd,permlevel)):
			error = await self.setversion(version=args[1])
	
		elif(cmd == "easter" and self.perm_valid(cmd,permlevel)):
			error = await self.easter(message.channel)
			
		elif(cmd =="easterranks" and self.perm_valid(cmd,permlevel)):
			error = await self.easterranks(message.channel)
		
		elif(cmd == "showissues" and self.perm_valid(cmd,permlevel)):
			error = await self.showissues(message.channel)

		elif(cmd == "reloadissues" and self.perm_valid(cmd,permlevel)):
			error = await self.reloadissues(message.channel)

		elif(cmd =="setcache" and self.perm_valid(cmd,permlevel)):
			error = await self.setcache(message.channel,args[1])
		
		elif(cmd =="endtrack" and self.perm_valid(cmd,permlevel)):
			error = await self.endtrack(message.channel)

		elif(cmd == "settrack" and self.perm_valid(cmd,permlevel)):
			error = await self.settrack(message.channel,message.mentions[0])

		elif(cmd == "gettrack" and self.perm_valid(cmd,permlevel)):
			error = await self.gettrack(message.channel)

		elif(cmd == "changelog" and self.perm_valid(cmd,permlevel)):
			embObj = discord.Embed(title="Latest Changes",description= self.dbhandler.get_from_misc("changelog"), color=self.SYSTEMCOLOR)
			error = await self.sendMsg(message.channel,embObj)

		elif(cmd == "setchangelog" and self.perm_valid(cmd,permlevel)):
			error = await self.setchangelog(message.channel, args[1])

		elif(cmd == "say" and self.perm_valid(cmd,permlevel)): #No embed as should rly just say stuff 
			error = await self.say(message.channel,args)

		elif (cmd == "setstatus" and self.perm_valid(cmd,permlevel)):
			error = await self.setstatus(message.content,args)
		
		elif (cmd =="execsql" and self.perm_valid(cmd,permlevel)):
			error = await self.execsql(channel=message.channel, cont=message.content, origlen=origlen)
		
		elif(cmd == "reload" and self.perm_valid(cmd,permlevel)):
			error = await self.reload(channel=message.channel)

		elif(cmd =="addcommand" and self.perm_valid(cmd,permlevel)):
			await self.addcommand(args)
			error = 0 #probably... not caring about any errors here lol

		elif(cmd == "setperm" and self.perm_valid(cmd,permlevel)):
			error = await self.setperm(user=message.mentions[0],perm_lev=args[2],own_perm_lev=permlevel)
		
		elif(cmd == "triggerannoy" and self.perm_valid(cmd,permlevel)):
			self.dbhandler.set_to_misc("annoyreaction", (not self.dbhandler.shouldAnnoy()))
			embObj = discord.Embed(title="Tracker", description=f" Turned reaction annoyance {('Off','On')[self.dbhandler.shouldAnnoy()]}",color = self.TRACKERCOLOR)
			await self.sendMsg(message.channel,embObj)
		
		elif(cmd == "mostmessages"):
			error = await self.mostmessages(channel=message.channel)


		elif(cmd == "togglecmd" and self.perm_valid(cmd,permlevel)):
			totogglecmd = ""
			try:
				totogglecmd = self.dbhandler.find_alias(args[1].strip())
				self.dbhandler._execComm(f'''UPDATE commands SET enabled={(1,0)[self.dbhandler.cmd_is_enabled(totogglecmd)]} WHERE cmdname=="{totogglecmd}"''')
			except IndexError:
				error = 3
			except:
				error = 2
		
		elif(cmd == "fixissue" and self.perm_valid(cmd,permlevel)):
			try:
				arg = int(args[1])
				self.dbhandler.fixissue(arg)
			except IndexError:
				error = 3
		
		elif(cmd == "testembed" and self.perm_valid(cmd,permlevel)):
			embObj = discord.Embed(title="title",description="descr",color=0x00ff00)
			embObj.add_field(name="test1",value="val1",inline=False)
			embObj.add_field(name="test2", value="val2", inline = True)
			await self.sendMsg(message.channel,embObj)
		
		elif(cmd == "info" and self.perm_valid(cmd,permlevel)):
			embObj = discord.Embed(title=self.client.user.name,description="Info about the greatest bot",color=self.SYSTEMCOLOR,url="http://brrr.nighmared.tech")
			embObj.set_thumbnail(url="https://repository-images.githubusercontent.com/324449465/a07d7880-4890-11eb-8bfa-a5db39975455")
			embObj.set_author(name="joniii")
			embObj.add_field(name="GH Repo",value ="http://brrr.nighmared.tech",inline=False)
			embObj.add_field(name="Version",value=self.dbhandler.get_from_misc("version"), inline=False)
			embObj.add_field(name="Uptime",value=self.uptime_tracker.getUptime())
			error = await self.sendMsg(message.channel,embObj)
		elif(cmd == "source" and self.perm_valid(cmd,permlevel)):
			embObj = discord.Embed(title="Source",description="http://brrr.nighmared.tech",color= self.SYSTEMCOLOR)
			error = await self.sendMsg(channel = message.channel,toSend=embObj)
		
		elif(cmd == "deletelast" and self.perm_valid(cmd,permlevel)):
			if(len(self.last_MSG) == 0):
				error = 3
			else:
				await self.last_MSG.pop().delete()
				error = 0

		elif(cmd == "deleteall" and self.perm_valid(cmd,permlevel)):
			while(len(self.last_MSG)>0):
				await self.last_MSG.pop().delete()

		elif(cmd == "deepsleep" and self.perm_valid(cmd,permlevel)):
			self.dbhandler.set_to_misc("standby",(1,0)[int(self.dbhandler.get_from_misc("standby"))])
			embObj = discord.Embed(
				title="DeepSleep Mode",
				description=f"{('leaving','entering')[int(self.dbhandler.get_from_misc('standby'))]} ~~Lockdown~~ deepsleep mode",
				color=self.SYSTEMCOLOR)
			await self.sendMsg(message.channel,embObj)
		
		elif(cmd == "neko" and self.perm_valid(cmd,permlevel)):
			embObj = discord.Embed(title="Neko",description=neko.getNeko(),color=self.NEKOCOLOR)
			await self.sendMsg(message.channel,embObj)
		elif(cmd == "createbackup" and self.perm_valid(cmd,permlevel)):
			error = self.dbhandler.create_backup()
			res = ("Created Backup of DB","Something went wrong")[error >0]
			embObj = discord.Embed(title="Backup", description=res,color = self.QUERYCOLOR)
			await self.sendMsg(channel=message.channel, toSend=embObj)

		else:
			error = 1
			if(not self.perm_valid(cmd,permlevel)):
				error = 4
		return 0 if error is None else error #quick fix until i properly refactored all cmds

	async def setversion(self,version)-> int:
		try:
			self.dbhandler.set_to_misc("version",version)
			error = 0
		except:
			error = 1			
		return error
	async def setchangelog(self,new_changelog)->int:
		try:
			self.dbhandler.set_to_misc("changelog",new_changelog)
			error = 0
		except:
			print("[commandhandler.py] UWU SHIT GONE WRONG IN SCL HANDLING")
			error = 1
	async def showissues(self,channel) -> int:
		res = self.dbhandler._execComm("select * from issues",True)
		embObj = discord.Embed(title="Issues",color=self.ISSUECOLOR)
		for id,title in res:
			embObj.add_field(name=id,value=title,inline=False)
		error = await self.sendMsg(channel,embObj)
		return error
	async def reloadissues(self,channel)->int:
		ls = issues.getIssues()
		if ls[0][0] == -1:
			error = 1
		else:
			self.dbhandler._execComm("DELETE FROM issues")
			for issue in ls:
				self.dbhandler.addIssue(issue)
			
			embObj = discord.Embed(title="Issues",description="Issues reloaded",color=self.ISSUECOLOR)
			error = await self.sendMsg(channel,embObj)
		return error
	async def help(self,channel,permlevel)-> int:
		cmds = self.dbhandler._execComm('''SELECT cmdname,helptext,alias,permlevel from commands where enabled==1 ORDER BY cmdname ASC, permlevel ASC''',raw=True)
		emotes = self.dbhandler._execComm('''SELECT value,desc FROM emotes ORDER BY id ASC''',raw=True)
		final_cmd = []
		for c in cmds:
			if(c[3]<=permlevel):
				final_cmd.append((c[0],c[1],c[2]))
		embObj = discord.Embed(title="Help", description="Displaying all available commands depending on callees permissionlevel",color=self.SYSTEMCOLOR)

		txt = []
		currFieldCont = ""
		currFieldIndex = 1
		for (cmdn,text,alias) in final_cmd:
			txt = f'`{self.PREFIX}{cmdn}` (`{self.PREFIX}{alias}`)\t {text.replace("_"," ")}\n'
			if(len(currFieldCont+txt)>self.EMBEDSIZELIMIT):
				embObj.add_field(name=f"Page {currFieldIndex}", value=currFieldCont)
				currFieldIndex+=1
				currFieldCont = txt
			else:
				currFieldCont+= txt
		
		embObj.add_field(name=f"Page {currFieldIndex}",value=currFieldCont)
		emote_val = ""
		for(emote,desc) in emotes:
			emote_val+= f"{emote}\t{desc}\n"
		embObj.add_field(name="Emotes",value=emote_val,inline=False)
		error = await self.sendMsg(channel,embObj)
		return error
	async def say(self,channel,args)-> int:
		resttxt = ""
		for a in args[1:]:
			resttxt += " "+a
		parts = resttxt.split("#")
		text = parts[0]
		try: repnum = int(parts[1])
		except: repnum = 0
		error = await self.sendMsg(channel,f"{text}")
		for counter in range(0,repnum):
			await self.sendMsg(channel,f"{text}")
		return error
	async def setstatus(self,cont,args)->int:
		type = 1
		splitbyquot = cont.split("\"")
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
				print(f"[commandhandler.py] (handling setstatus) | type={type} ")
		await self.client.change_presence(activity=discord.Activity(name=stringarg,type= type))
		return 0
	async def addcommand(self,args):
		self.dbhandler._execComm(
			f'''
			INSERT INTO commands(
				"cmdname",
				"permlevel",
				"helptext",
				"alias",
				"enabled"
				)
			VALUES(
				"{args[1]}",
				{args[2]},
				"{args[3]}",
				"{args[4]}",
				"{args[5]}"
				)''')
	async def setperm(self,user,perm_lev,own_perm_lev:int):
		if(perm_lev>=own_perm_lev):
			error = 3 #make sure you cant promote yourself or anyone else over your own rank
		else:
			error = self.dbhandler.set_perm(user, newpermlev=perm_lev)
		return error
	async def execsql(self,channel,cont:str,origlen:int)->int:
		res = self.dbhandler._execComm(cont[(origlen+1):].strip())
		if(res !=-10):
			embObj = discord.Embed(title="Query Result",color=self.QUERYCOLOR)
			if(len(res)>self.EMBEDSIZELIMIT):
				res2 = res.split("\n")
				curr_page_num = 1
				curr_page_cont = ""
				for line in res2:
					if(line.strip() == ""):
						continue
					if(len(curr_page_cont+line)+2>self.EMBEDSIZELIMIT):
						embObj.add_field(name=f"Page {curr_page_num}",value=curr_page_cont,inline=False)
						curr_page_cont = ""
						curr_page_num+=1
					else:
						curr_page_cont+=line+"\n"
				embObj.add_field(name=f"Page {curr_page_num}", value=curr_page_cont)
			else:
				embObj.add_field(name="Output",value=res)
			await self.sendMsg(channel,embObj)
		return 0
	async def reload(self,channel):
		embObj = discord.Embed(title="Reloading...",description="let's hope this doesn't fuck anything up...",color=self.SYSTEMCOLOR)
		await self.sendMsg(channel,embObj)
		return 99


	async def msgarchive(self,channel)-> int:	
		msgls = self.msgs.sendable()
		if(len(msgls)== ""):
			error = 2
		else:
			embObj = discord.Embed(title="Tracker",description=f"Recent messages by {msgls[0].author.nick}",color = self.TRACKERCOLOR)
			fieldStr = ""
			for msg in msgls:
				fieldStr+=f"{str(msg.created_at)[:-4]} {msg.author.nick}-> {msg.channel.name}: {msg.content[:100]}\n"
			embObj.add_field(name="Messagehistory",value=fieldStr,inline=True)

			error = await self.sendMsg(channel, embObj)
		return error
	async def setcache(self,channel,cachelen)->int:
		try:
			newLen = int(cachelen)
			newLen = self.msgs.set_len(newLen)
			embObj = discord.Embed(title="Tracker",description=f"updated cache length to {newLen}",color=self.TRACKERCOLOR)
			error = await self.sendMsg(channel,embObj)
		except Exception:
			error = 1
		return error
	async def settrack(self,channel,user)->int:
		try:
			self.toTrackID = user.id
			self.toTrackName = user.mention
			self.msgs.set_user(self.toTrackName)
			embObj = discord.Embed(title="Tracker",description=f"updated tracked user to {self.toTrackName}",color = self.TRACKERCOLOR)
			error = await self.sendMsg(channel,embObj)
		except IndexError:
			error = 3
		except Exception:
			error = 1
		return error
	async def endtrack(self,channel)->int:
		toTrackID = 0
		toTrackName = "nobody"
		self.msgs.set_user(toTrackName)
		embObj = discord.Embed(title="Tracker",description="stopped tracking",color=self.TRACKERCOLOR)
		error = await self.sendMsg(channel,embObj)
	async def gettrack(self,channel)->int:
		embObj = discord.Embed(
			title="Tracker",
			description=f"currently tracking {self.toTrackName}",
			color = self.TRACKERCOLOR
			)
		error = await self.sendMsg(channel=channel,toSend=embObj)
		return error
	
	async def easter(self,channel) -> int:
		embObj = discord.Embed(title="What is this?", description="cmljZXB1cml0eXRlc3QubW9iaS9bZGlzY29yZG5hbWVfb2ZfMjIzOTMyNzc1NDc0OTIxNDcyXS5odG1s")
		error = await self.sendMsg(toSend=embObj,channel=channel)
		await self.last_MSG.pop(-1).delete(delay=.5)
		return error
	async def easterranks(self,channel)-> int:
		txt = self.dbhandler.get_from_misc("easter")
		embObj = discord.Embed(title="Easter Egg Hunt leaderboard", description=txt)
		error = await self.sendMsg(toSend= embObj, channel = channel)
		return error
	async def mostmessages(self,channel)->int:
		res = self.dbhandler.get_most_messages()
		embObj = discord.Embed(title="Message Leaderboard",description="Showing which user has sent the most messages", color=self.TRACKERCOLOR)
		field_value = ""
		rank = 1
		field_count = 1
		for entry in res:
			to_add = f"> {str(rank).rjust(3)}. {str(entry[0]).rjust(32)} {str(entry[1]).rjust(5)}\n"
			if len(field_value+to_add)>self.EMBEDSIZELIMIT:
				if(field_count>24):
					break
				embObj.add_field(name=f"Page {field_count}",value=field_value)
				field_count += 1
				field_value = to_add
			else:				
				field_value += to_add
			rank += 1
		embObj.add_field(name=f"Page {field_count}",value=field_value)
		error = await self.sendMsg(channel,embObj)
		return error

class fake_msg:
	def __init__(self,message):
		msg_cont = message.content
		cmdlen = len(message.content.split(" ")[0])
		self.content = message.content[cmdlen:]
		self.author = message.author
		self.channel = message.channel
		self.mentions = message.mentions
		self.id = message.id
	def setcont(self,newcont:str):
		self.content = newcont
	