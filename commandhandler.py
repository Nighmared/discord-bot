import subprocess
from discord import colour
from discord.embeds import Embed
from sqlite3 import OperationalError
import dbhandler
import discord
import issues
import msglist
import neko
import nhentai

IMPORTS = (neko,issues,nhentai)



class commandhandler:
	ISSUECOLOR = 0x00f0f0 #lightblue
	TRACKERCOLOR = 0x660066 #pinkish
	SYSTEMCOLOR = 0x009900# green
	QUERYCOLOR = 0xffcc00 # yellow
	NEKOCOLOR = 0xcc6699
	NORMALCOLOR = 0x000000 # black
	ERRORCOLOR = 0xff0000 # red
	FIELDSIZELIMIT = 1024
	EMBEDSIZELIMIT = 5950
	MAXNUMBEROFEMBEDS = 25
	ALLOWEDSOURCEFILES = {
		"dbhandler":"dbhandler.py",
		"db":"dbhandler.py",
		"issues":"issues.py",
		"msglist":"msglist.py",
		"neko":"neko.py",
		"nhentai":"nhentai.py",
		"uptime":"uptime.py",
		"push":"push.sh",
		"runner":"runner.sh",
		"main":"bot.py",
		"bot":"bot.py",
		"commandhandler":"commandhandler.py",
		"cmd":"commandhandler.py",
		"msghandler":"msghandler.py",
		"msg": "msghandler.py",

	}



	def __init__(self,
	dbhandler:dbhandler.dbhandler,
	msgs:msglist,
	PREFIX:str,
	time_tracker,
	client:discord.Client,
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
		self.nh_handler = nhentai.handler(self.dbhandler)


	def perm_valid(self,cmd:str,permlevel:int)->bool:
		return permlevel >= self.dbhandler.get_cmd_perm(cmd)
	
	async def sendMsg(self,channel,toSend,file=None,callee = "INVALID"):
		try:
			if(type(toSend) == discord.embeds.Embed):
				if callee == "INVALID":
					toSend.set_footer(text=f"Answering to {self.curr_msg.author.name}\n <fix footer for dis cmd>")
				else:
					toSend.set_footer(text = f"Answering to {callee}")
				if file is not None:
					self.last_MSG.append(await channel.send(file=file,embed=toSend))
				else:
					self.last_MSG.append(await channel.send(embed=toSend))
			else: #only the case for say command
				self.last_MSG.append(await channel.send(str(toSend)))
			return 0
		except discord.Forbidden:
			return 5
	


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

		if not self.perm_valid(cmd,permlevel):
			return 4

		if(cmd == "msgarchive"):
			error,embObj = await self.msgarchive(message.channel)
			if embObj is not None:
				err2 = await self.sendMsg(message.channel,embObj)	
				error = (err2,error)[error == 0]
		elif(cmd == "help"):
			error,embObj = await self.help(message)
			if embObj is not None:
				err2 = await self.sendMsg(message.channel,embObj)	
				error = (err2,error)[error == 0]
			
		elif(cmd =="setversion"):
			error = await self.setversion(version=args[1])
	
		elif(cmd == "easter"):
			error,embObj = await self.easter(message)
			if embObj is not None:
				err2 = await self.sendMsg(message.channel,embObj)	
				error = (err2,error)[error == 0]
			
		elif(cmd =="easterranks"):
			error.embObj = await self.easterranks(message)
		
		elif(cmd == "showissues"):
			error = await self.showissues(message.channel)

		elif(cmd == "reloadissues"):
			error = await self.reloadissues(message.channel)

		elif(cmd =="setcache"):
			error = await self.setcache(message.channel,args[1])
		
		elif(cmd =="endtrack"):
			error,embObj = await self.endtrack(message)
			if embObj is not None:
				err2 = await self.sendMsg(message.channel,embObj)	
				error = (err2,error)[error == 0]

		elif(cmd == "settrack"):
			error = await self.settrack(message.channel,message.mentions[0])

		elif(cmd == "gettrack"):
			error,embObj = await self.gettrack(message)
			if embObj is not None:
				err2 = await self.sendMsg(message.channel,embObj)	
				error = (err2,error)[error == 0]

		elif(cmd == "changelog"):
			error,embObj = await self.changelog(message)
			if embObj is not None:
				err2 = await self.sendMsg(message.channel,embObj)	
				error = (err2,error)[error == 0]

		elif(cmd == "setchangelog"):
			error = await self.setchangelog( args[1])

		elif(cmd == "say"): #No embed as should rly just say stuff 
			error = await self.say(message.channel,args)

		elif (cmd == "setstatus"):
			error = await self.setstatus(message.content,args)
		
		elif (cmd =="execsql"):
			error,embObj = await self.execsql(message)
			if embObj is not None:
				err2 = await self.sendMsg(message.channel,embObj)	
				error = (err2,error)[error == 0]
		
		elif(cmd == "reload"):
			error,embObj = await self.reload(message)
			if await self.sendMsg(channel=message.channel, toSend = embObj) >0:
				error = 1 #DONT FIX THIS, IS SPECIAL FOR RELOAD


		elif(cmd =="addcommand"):
			(error, embObj) = await self.addcommand(message)
			if embObj is not None:
				err2 = await self.sendMsg(message.channel,embObj)	
				error = (err2,error)[error == 0]
				

		elif(cmd == "setperm"):
			error = await self.setperm(user=message.mentions[0],perm_lev=args[2],own_perm_lev=permlevel)
		
		elif(cmd == "triggerannoy"):
			self.dbhandler.set_to_misc("annoyreaction", (not self.dbhandler.shouldAnnoy()))
			embObj = discord.Embed(title="Tracker", description=f" Turned reaction annoyance {('Off','On')[self.dbhandler.shouldAnnoy()]}",color = self.TRACKERCOLOR)
			await self.sendMsg(message.channel,embObj)
		
		elif(cmd == "mostmessages"):
			error, embObj = await self.mostmessages(message)
			if embObj is not None:
				err2 = await self.sendMsg(message.channel,embObj)	
				error = (err2,error)[error == 0]
		elif(cmd == "superdelete"):
			error = await self.superdelete(msg = await message.channel.fetch_message(message.reference.message_id))

		elif(cmd == "togglecmd"):
			totogglecmd = ""
			try:
				totogglecmd = self.dbhandler.find_alias(args[1].strip())
				self.dbhandler._execComm(f'''UPDATE commands SET enabled={(1,0)[self.dbhandler.cmd_is_enabled(totogglecmd)]} WHERE cmdname=="{totogglecmd}"''')
			except IndexError:
				error = 3
			except:
				error = 2
		
		elif(cmd == "fixissue"):
			error,embObj = await self.fixissue(message)
			

		
		elif(cmd == "info"):
			error,embObj = await self.info(message)
			if embObj is not None:
				err2 = await self.sendMsg(message.channel,embObj)	
				error = (err2,error)[error == 0]
		elif(cmd == "ping"):
			error = await self.ping(channel=message.channel)
		elif(cmd == "source"):
			embObj = discord.Embed(title="Source",description="http://brrr.nighmared.tech",color= self.SYSTEMCOLOR)
			error = await self.sendMsg(channel = message.channel,toSend=embObj)
		
		elif(cmd == "deletelast"):
			error, embObj = await self.deletelast(message)
			if embObj is not None:
				err2 = await self.sendMsg(message.channel,embObj)	
				error = (err2,error)[error == 0]
			
		elif(cmd == "deleteall"):
			error,embObj = await self.deleteall(message)
			if embObj is not None:
				err2 = await self.sendMsg(message.channel,embObj)	
				error = (err2,error)[error == 0]
		elif(cmd == "deepsleep"):
			error,embObj = await self.deepsleep(message)
			if embObj is not None:
				err2 = await self.sendMsg(message.channel,embObj)	
				error = (err2,error)[error == 0]
		elif(cmd == "neko"):
			error,embObj = await self.neko(message)
			if embObj is not None:
				err2 = await self.sendMsg(message.channel,embObj)	
				error = (err2,error)[error == 0]
		elif(cmd == "nhentai"):
			error,embObj,f = await self.nhentai(message)
			if embObj is not None:
				err2 = await self.sendMsg(message.channel,embObj,file=f,callee=message.author.nick)	
				error = (err2,error)[error == 0]
		elif(cmd == "togglensfw"):
			error = await self.togglensfw(message.channel)
		elif(cmd == "nhentaiblock"):
			error = await self.nhentaiblock(args)
		elif(cmd == "nhentailog"):
			error = await self.nhentailog(message.channel)
		elif(cmd == "createbackup"):
			error,embObj = await self.createbackup(message)
			await self.sendMsg(channel=message.channel, toSend=embObj)
		elif(cmd == "showsourcecode"):
			error = await self.showsourcecode(message.channel,args)
		elif(cmd == "banner"):
			error,embObj = await self.banner(message)
			if embObj is not None:
				err2 = await self.sendMsg(message.channel,embObj)	
				error = (err2,error)[error == 0]
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
	async def changelog(self,message:discord.Message)->tuple:
		try:
			embObj = discord.Embed(title="Latest Changes",description= self.dbhandler.get_from_misc("changelog"), color=self.SYSTEMCOLOR)
			return (0,embObj)
		except OperationalError:
			embObj = discord.Embed(title="Latest Changes", description="-- Something went wrong with DB --",color =self.SYSTEMCOLOR)
			return (1,embObj)
	async def createbackup(self,message:discord.Message)->tuple:
		error = self.dbhandler.create_backup()
		res = ("Created Backup of DB","Something went wrong")[error >0]
		embObj = discord.Embed(title="Backup", description=res,color = self.QUERYCOLOR)
		return (error,embObj)
	async def deepsleep(self,message:discord.Message)->tuple:
		try:
			self.dbhandler.set_to_misc("standby",(1,0)[int(self.dbhandler.get_from_misc("standby"))])
			embObj = discord.Embed(
				title="DeepSleep Mode",
				description=f"{('leaving','entering')[int(self.dbhandler.get_from_misc('standby'))]} ~~Lockdown~~ DeepSleep mode",
				color=self.SYSTEMCOLOR)
			return (0,embObj)
		except OperationalError:
			embObj = discord.Embed(title="DeepSleep Mode", description = "-- Something went wrong with DB --", color = self.SYSTEMCOLOR)
			return (1,embObj)
	async def deleteall(self,message:discord.Message)->tuple:
		while(len(self.last_MSG)>0):
			try:
				await self.last_MSG.pop().delete()
			except:
				continue
		return (0,None)
	async def deletelast(self,message:discord.Message)->tuple:
		args = message.content[1:].split(" ")
		if(len(self.last_MSG) == 0):
			error = 3
		else:
			if len(args)>1 and args[1].isnumeric:
				num_delete = int(args[1])
			else:
				num_delete = 1
			while(num_delete>0):
				if len(self.last_MSG) == 0:
					break
				try:
					await self.last_MSG.pop().delete()
					num_delete -= 1
				except discord.NotFound:
					continue
			error = 0
		return (error,None)
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
	async def fixissue(self,message:discord.Message)->tuple:
		args = message.content[1:].split(" ")
		try:
			arg = int(args[1])
			self.dbhandler.fixissue(arg)
			error = 0
		except IndexError:
			error = 3
		return (error,None)
	async def help(self,message:discord.Message)-> int:
		try:
			channel = message.channel
			args = message.content[1:].split(" ")
			permlevel = self.dbhandler.get_perm_level(message.author.id)

			if len(args)>1 and args[1].isnumeric:
				permlevel = int(args[1])
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
				if(len(currFieldCont+txt)>self.FIELDSIZELIMIT):
					embObj.add_field(name=f"Page {currFieldIndex}", value=currFieldCont)
					currFieldIndex+=1
					currFieldCont = txt
				else:
					currFieldCont+= txt
			if currFieldCont == "" and currFieldIndex == 1: currFieldCont = "[Well.. nothing :/]" #lol
			embObj.add_field(name=f"Page {currFieldIndex}",value=currFieldCont)
			emote_val = ""
			for(emote,desc) in emotes:
				emote_val+= f"{emote}\t{desc}\n"
			embObj.add_field(name="Emotes",value=emote_val,inline=False)
			return (0,embObj)
		except Exception as e:
			embObj = discord.Embed(title="Help",description=str(e),color = self.ERRORCOLOR)
			return (1,embObj)
	async def info(self,message:discord.Message)-> int:
		try:
			embObj = discord.Embed(title=self.client.user.name,description="Info about the greatest bot",color=self.SYSTEMCOLOR,url="http://brrr.nighmared.tech")
			embObj.set_thumbnail(url="https://repository-images.githubusercontent.com/324449465/a07d7880-4890-11eb-8bfa-a5db39975455")
			embObj.set_author(name="joniii")
			embObj.add_field(name="GH Repo",value ="http://brrr.nighmared.tech",inline=False)
			embObj.add_field(name="Version",value=self.dbhandler.get_from_misc("version"), inline=False)
			embObj.add_field(name="Uptime",value=self.uptime_tracker.getUptime())
			return (0,embObj)
		except Exception as e:
			embObj = discord.Embed(title="Info",description = str(e), color = self.ERRORCOLOR)
			return (1,embObj)
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
	async def showsourcecode(self,channel,args)->int:
		if len(args)<1:
			error = 3
		else:
			module_name = args[1]
			if module_name in self.ALLOWEDSOURCEFILES.keys():
				line_indx = 0
				file = open(self.ALLOWEDSOURCEFILES[module_name],mode='r')
				lines = file.read().split("\n")
				file.close()
				num_lines = len(lines)
				syntax_keyword = "py" if self.ALLOWEDSOURCEFILES[module_name].endswith("py") else "sh"
				if len(args)>2 and args[2].isnumeric:
					line_indx = int(args[2]) #start at later line
				if(line_indx>=num_lines):
					error = 3
				else:
					msg =f"{'`'*3}{syntax_keyword}\n"
					while line_indx<num_lines and len(msg+lines[line_indx])<1945:
						msg+= f"{str(line_indx+1).rjust(3)}| {lines[line_indx]}\n"
						line_indx+=1
					msg += "\n"+"`"*3
					error = await self.sendMsg(channel=channel, toSend=msg)

			else:
				error = 4
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
	async def addcommand(self,message)->tuple:
		try:
			args = message.content[1:].split(" ")
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
			return (0, None)
		except (OperationalError, IndexError):
			embObj = discord.Embed(title="Addcommand", description=f"Usage: {self.PREFIX}addcommand <cmdname:str> <permlevel:int> <help_text:str> <alias:str> <enabled:[0,1]>", color = self.QUERYCOLOR)
			return (3, embObj)

	async def setperm(self,user,perm_lev,own_perm_lev:int):
		if(int(perm_lev)>=own_perm_lev):
			error = 3 #make sure you cant promote yourself or anyone else over your own rank
		else:
			error = self.dbhandler.set_perm(user, newpermlev=perm_lev)
		return error
	async def execsql(self,message:discord.Message)->tuple:
		cont = message.content
		origlen = len(cont[1:].split(" ")[0].lower())
		query = cont[(origlen+1):].strip()
		try:
			res = self.dbhandler._execComm(query)
		except OperationalError:
			print("[commandhandler.py] Something went wrong with sqlite")
			embObj = discord.Embed(title="ExecSQL",description = "-- Something went wrong with DB --",color=self.ERRORCOLOR)
			return (3,embObj) # command is fuckd up probably
		if(res !=-10):
			embObj = discord.Embed(title="Query Result",description = ">"+query,color=self.QUERYCOLOR)
			embed_len = 100
			if(len(res)>self.FIELDSIZELIMIT):
				res2 = res.split("\n")
				curr_page_num = 1
				curr_page_cont = ""
				for line in res2:
					if(line.strip() == ""):
						continue
					if(len(curr_page_cont+line)+2>self.FIELDSIZELIMIT):
						embed_len  += len(curr_page_cont)
						if embed_len> self.EMBEDSIZELIMIT:
							break
						embObj.add_field(name=f"Page {curr_page_num}",value=curr_page_cont,inline=False)
						curr_page_cont = line+"\n"
						curr_page_num+=1
					else:
						curr_page_cont+=line+"\n"
				if len(curr_page_cont) >0 and embed_len<=self.EMBEDSIZELIMIT:
					embObj.add_field(name=f"Page {curr_page_num}", value=curr_page_cont)
			else:
				embObj.add_field(name="Output",value=res)
			#print(embed_len)
			return (0,embObj)
	async def reload(self,message):
		embObj = discord.Embed(title="Reloading...",description="let's hope this doesn't fuck anything up...",color=self.SYSTEMCOLOR)
		return (99,embObj)

	async def ping(self,channel)-> int:
		embObj = discord.Embed(title="Ping",description="Pong!", color= self.SYSTEMCOLOR)
		return await self.sendMsg(channel=channel, toSend=embObj)
	async def msgarchive(self,message)-> tuple:
		try:	
			msgls = self.msgs.sendable()
			if(len(msgls)== ""):
				error = 2
			else:
				embObj = discord.Embed(title="Tracker",description=f"Recent messages by {msgls[0].author.nick}",color = self.TRACKERCOLOR)
				fieldStr = ""
				for msg in msgls:
					fieldStr+=f"{str(msg.created_at)[:-4]} {msg.author.nick}-> {msg.channel.name}: {msg.content[:100]}\n"
				embObj.add_field(name="Messagehistory",value=fieldStr,inline=True)
			return (0,embObj)
		except Exception as e:
			embObj = discord.Embed(title="Tracker",description = f"Something went wrong, prolly not tracking anyone rn \n➥{str(e)}",color = self.ERRORCOLOR)
			return (1,embObj)
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
	async def endtrack(self,message:discord.Message)->tuple:
		toTrackID = 0
		toTrackName = "nobody"
		self.msgs.set_user(toTrackName)
		embObj = discord.Embed(title="Tracker",description="stopped tracking",color=self.TRACKERCOLOR)
		return (0,embObj)
	async def gettrack(self,message:discord.Message)->tuple:
		embObj = discord.Embed(
			title="Tracker",
			description=f"currently tracking {self.toTrackName}",
			color = self.TRACKERCOLOR
			)
		return (0,embObj)
	
	async def easter(self,message:discord.Message) -> tuple:
		embObj = discord.Embed(title="What is this?", description="cmljZXB1cml0eXRlc3QubW9iaS9bZGlzY29yZG5hbWVfb2ZfMjIzOTMyNzc1NDc0OTIxNDcyXS5odG1s")
		error = await self.sendMsg(toSend=embObj,channel=message.channel)
		await self.last_MSG.pop(-1).delete(delay=.5)
		return (error,None)
	async def easterranks(self,message: discord.Message)-> tuple:
		try: 
			txt = self.dbhandler.get_from_misc("easter")
			embObj = discord.Embed(title="Easter Egg Hunt leaderboard", description=txt)
			return (0,embObj)
		except OperationalError:
			embObj = discord.Embed(title="Easter Egg Hunt leaderboard", description="-- Something went wrong with DB --", color = self.ERRORCOLOR)
			return (1,embObj)
	async def mostmessages(self,message:discord.Message)->tuple:
		try:
			res = self.dbhandler.get_most_messages()
			embObj = discord.Embed(title="Message Leaderboard",description="Showing which user has sent the most messages", color=self.TRACKERCOLOR)
			field_value = ""
			rank = 1
			for entry in res:
				to_add = f"{str(rank).rjust(3)}. {str(entry[0]).rjust(32)} {str(entry[1]).rjust(5)}\n"
				if len(field_value+to_add)>self.FIELDSIZELIMIT:
					embObj.add_field(name=f"Ranking",value=field_value,inline=False)
					field_value = ""
					break
				else:				
					field_value += to_add
				rank += 1
			if field_value !="":
				embObj.add_field(name=f"Ranking",value=field_value,inline=False)
			return (0,embObj)
		except Exception as e:
			embObj = discord.Embed(title="Message Leaderboard", description = str(e), color =self.ERRORCOLOR)
			return (1,embObj)
	async def superdelete(self,msg : discord.Message):
		try:
			await msg.delete()
			error = 0
		except discord.Forbidden:
			error = 4
		except discord.NotFound:
			error = 2
		except discord.HTTPException:
			error = 1
		return error
	async def neko(self,message:discord.Message)->tuple:
		try:
			embObj = discord.Embed(title="Neko",description=neko.getNeko(),color=self.NEKOCOLOR)
			return (0,embObj)
		except Exception as e:
			embObj = discord.Embed(title="Neko",description = str(e), color =self.ERRORCOLOR)
			return (1,embObj)
	async def nhentai(self,message:discord.Message)->tuple:
		if not (type(message.channel) != discord.channel.TextChannel or message.channel.is_nsfw()):
				return (2,None,None)

		args = message.content[1:].split(" ")
		user_pl = self.dbhandler.get_perm_level(message.author.id)
		nsfw = int(self.dbhandler.get_from_misc("nsfw"))!=0
		link = ""
		error = 0
		img_id = -1
		sigma = int(self.dbhandler.get_from_misc("blur_sigma"))
		if len(args)>1 and args[1].isnumeric and user_pl>self.dbhandler.get_cmd_perm("nhentai"):
			img_id = args[1]
			link = self.dbhandler.get_nhentai_path_by_id(img_id)[0]
			if link == -1:
				link = self.nh_handler.get_img(sigma,img_id)
		else:
			sigma = int(self.dbhandler.get_from_misc("blur_sigma"))
			link = self.nh_handler.get_img(sigma)
		if(error==0):
			if nsfw:
				link = f"{link.rstrip('.blurred.jpg')}.jpg"
			img_id = link.rstrip(".blurred.jpg")
			embObj = discord.Embed(title="nHentai Random Cover",description=img_id,color = self.NEKOCOLOR)
			try:
				file_to_send = discord.File(link,filename="SPOILER_FILE.jpg",spoiler=True)
			except FileNotFoundError: #accidentally pushed dumb shit; this will rarely occur but prolly fixes it
				link2 = link.rstrip(".blurred.jpg")+".jpg"
				print("[commandhandler.py] nh command; lin2 in catch block = ",link2)

				self.nh_handler._blur(link2,sigma)
				file_to_send = discord.File(link,filename="SPOILER_FILE.jpg",spoiler=True)
			embObj.set_image(url="attachment://SPOILER_FILE.jpg")
		nh_log = open("nhentai/log.txt","a")
		nh_log.write(f">Sent nhentai/{str(img_id).lstrip('nhentai/')}\n")
		nh_log.close()
		return (0,embObj,file_to_send)
	async def togglensfw(self,channel):
		new_state = self.dbhandler.toggle_nsfw()
		embObj = discord.Embed(title="Toggled NSFW",color=self.NEKOCOLOR,description=f"Turned explicit content {('off','on')[new_state]}")
		error = await self.sendMsg(toSend=embObj,channel=channel)
		return error
	async def nhentaiblock(self,args)->int:
		if len(args)>1 and args[1].isnumeric:
			error = self.nh_handler.nhentai_block(args[1])
		else:
			error =3
		return error
	async def nhentailog(self,channel)->int:
		log_len = min(int(self.dbhandler.get_from_misc("nh_log_len")),48)
		log_lines = open("nhentai/log.txt").readlines()
		embObj = discord.Embed(title="nhentai log",color=self.NEKOCOLOR)
		field_cont = ""
		for line in log_lines[-log_len:]:
			field_cont+= line+"\n"
		embObj.add_field(name="Entries",value=field_cont)
		error = await self.sendMsg(channel=channel,toSend=embObj)
		#log management
		if len(log_lines)>500:
			print("[commandhandler.py] (nhl) trying to rotate log")
			open("nhentai/log.txt.old","w").writelines(log_lines) #lol idk how this is gonna end
			curr_log = open("nhentai/log.txt","w")
			curr_log.write("")
			curr_log.close()
		
		return error
	async def banner(self,message)-> int:
		try:
			channel,guild = message.channel,message.guild
			banner_url = guild.banner_url
			embObj = discord.Embed(title="Banner",description=guild.name, color=self.NORMALCOLOR)
			embObj.set_image(url=banner_url)
			return (0,embObj)
		except:
			return (1,None)
		