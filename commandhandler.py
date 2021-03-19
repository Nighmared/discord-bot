import subprocess
from discord import colour
from discord import embeds
from discord.embeds import Embed, EmbedProxy
from sqlite3 import OperationalError
import logging

from discord.utils import _bytes_to_base64_data
import dbhandler
import discord
import issues
import msglist
import neko
import nhentai
import inspirobot
import meme

IMPORTS = (neko,issues,nhentai,inspirobot,meme)



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
		"inspire":"inspirobot.py",

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


		self.cmd_handling_funcs = {
			"addcommand":self.addcommand,
			"banner":self.banner,
			"changelog":self.changelog,
			"createbackup":self.createbackup,
			"deepsleep":self.deepsleep,
			"deleteall":self.deleteall,
			"deletelast":self.deletelast,
			"easter":self.easter,
			"easterranks":self.easterranks,
			"endtrack":self.endtrack,
			"execsql":self.execsql,
			"fixissue":self.fixissue,
			"gettrack":self.gettrack,
			"help":self.help,
			"info":self.info,
			"inspire":self.inspire,
			"mostmessages":self.mostmessages,
			"msgarchive":self.msgarchive,
			"neko":self.neko,
			"nhentai":self.nhentai,
			"nhentaiblock":self.nhentaiblock,
			"nhentailog":self.nhentailog,
			"ping":self.ping,
			"reload":self.reload,
			"reloadissues":self.reloadissues,
			"say":self.say,
			"setcache":self.setcache,
			"setchangelog":self.setchangelog,
			"setperm":self.setperm,
			"setstatus":self.setstatus,
			"settrack":self.settrack,
			"setversion":self.setversion,
			"showissues":self.showissues,
			"showsourcecode":self.showsourcecode,
			"source":self.source,
			"stalk":self.stalk,
			"superdelete":self.superdelete,
			"togglecmd":self.togglecmd,
			"togglensfw":self.togglensfw,
			"triggerannoy":self.triggerannoy,
			"makememe":self.makememe,
			"add_meme_template":self.add_meme_template,
		}


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
	


	async def commandHandler(self,message:discord.Message,permlevel:int) -> int:
		self.curr_msg = message
		args = message.content[1:].split(" ")
		cmd = args[0].lower()
		cmd = self.dbhandler.find_alias(cmd)
		if(cmd == ""):
			logging.warning(f"{message.author.name}#{message.author.discriminator} tried to use an invalid command")
			return 3
		if not self.dbhandler.cmd_is_enabled(cmd):
			error = 4
			logging.warning(f"{message.author.name}#{message.author.discriminator} tried to use a disabled command ({cmd})")
			#print(f"[commandhandler.py] disabled/invalid cmd: {cmd}")
			return error
		error = 0

		if not self.perm_valid(cmd,permlevel):
			return 4
		
		if cmd == "reload":
			error,embObj = await self.reload(message)
			if await self.sendMsg(channel=message.channel, toSend = embObj) >0:
				error = 1 #DONT FIX THIS, IS SPECIAL FOR RELOAD
			return error
		#general case
		res = await self.cmd_handling_funcs[cmd](message)
		if len(res) == 2:
			error, embObj = res
			file = None
		else:
			error,embObj, file = res
		if embObj is not None:
			try:
				callee = message.author.nick if message.author.nick is not None else message.author.name
			except AttributeError:
				callee = message.author.name
			err2 = await self.sendMsg(message.channel,embObj,callee=callee, file=file)	
			error = (error, err2)[error == 0]
		return error

	async def addcommand(self,message:discord.Message)->tuple:
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
	async def add_meme_template(self,message:discord.Message)->tuple:
		try:
			args = message.content[1:].split(" ")
			template_name = args[2]
			template_id = args[3]
			self.dbhandler.add_meme_template(template_name,int(template_id))
			return (0,None)
		except Exception as e:
			print("[dbhandler.py] add_meme_template: ",str(e))
			return (1,None)
	async def banner(self,message:discord.Message)-> tuple:
		try:
			channel,guild = message.channel,message.guild
			banner_url = guild.banner_url
			embObj = discord.Embed(title="Banner",description=guild.name, color=self.NORMALCOLOR)
			embObj.set_image(url=banner_url)
			return (0,embObj)
		except:
			return (1,None)
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
	async def endtrack(self,message:discord.Message)->tuple:
		toTrackID = 0
		toTrackName = "nobody"
		self.msgs.set_user(toTrackName)
		embObj = discord.Embed(title="Tracker",description="stopped tracking",color=self.TRACKERCOLOR)
		return (0,embObj)
	async def execsql(self,message:discord.Message)->tuple:
		cont = message.content
		origlen = len(cont[1:].split(" ")[0].lower())
		query = cont[(origlen+1):].strip()
		try:
			res = self.dbhandler._execComm(query)
		except OperationalError as e:
			logging.error(f"Something went wrong with the DB (Query: {query} ")
			#print("[commandhandler.py] Something went wrong with sqlite")
			embObj = discord.Embed(title="ExecSQL",description = str(e),color=self.ERRORCOLOR)
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
			return (0,embObj)
		else:
			return (0,None)
	async def fixissue(self,message:discord.Message)->tuple:
		args = message.content[1:].split(" ")
		try:
			arg = int(args[1])
			self.dbhandler.fixissue(arg)
			error = 0
		except IndexError:
			error = 3
		return (error,None)
	async def gettrack(self,message:discord.Message)->tuple:
		embObj = discord.Embed(
			title="Tracker",
			description=f"currently tracking {self.toTrackName}",
			color = self.TRACKERCOLOR
			)
		return (0,embObj)
	async def help(self,message:discord.Message)-> tuple:
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
	async def info(self,message:discord.Message)-> tuple:
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
	async def inspire(self,message:discord.Message)->tuple:
		error, cont = inspirobot.get_img_url()
		if error>0:
			embObj = discord.Embed(title="Inspire",description=cont,color=self.ERRORCOLOR)
		else:
			embObj = discord.Embed(title="Inspire", description="Newly generated inspirobot.me quote",url="https://inspirobot.me",color=self.NEKOCOLOR)
			embObj.set_image(url=cont)
		return (error,embObj)
	async def makememe(self,message:discord.Message)->tuple:
		try:
			probable_sqli = message.content.count("\"")>2
			space_split_args = message.content.split(" ")
			caption = message.content.split("\"")[1]
			for x in ("\'","--",";","*",):
				if x in caption:
					probable_sqli = True
					break
			
			if probable_sqli:
				embObj = discord.Embed(title="makememe",description="This seems sus af..",color=self.QUERYCOLOR)
				embObj.add_field(name="WHODIDTHIS",value=message.author.mention)
				embObj.add_field(name="command",value=message.content[:2000])
				embObj.add_field(name="Tag for easy search",value="GGB SQLI")
				return (3,embObj)
			template_name = space_split_args[1]
			top_caption = False
			if space_split_args[2].strip().isnumeric():
				top_caption = int(space_split_args[2].strip())==1
			error, img_url, error_descr, post_url = meme.get_meme(template_name,caption,self.dbhandler,top_caption )
		except IndexError:
			error = 3
			error_descr = "Invalid Usage"	
		if error == 3:  #-> invalid template
			embObj = discord.Embed(title="makememe",description=error_descr,color=self.ERRORCOLOR)
			templates = ""
			for t in meme.TEMPLATE_IDS.keys():
				templates += t+", "
			embObj.add_field(name="Possible template names:",value=templates)
			embObj.add_field(name="Usage",value=f"{self.PREFIX}makememe <template_name> [<1 or 0 to determine location of text>] \"some caption\"\n Example: {self.PREFIX}makememe spongebob_mocking \"spam is not nsfw\"", inline=False)
			return (3,embObj)
		elif error == 1:
			embObj = discord.Embed(title="makememe", description=error_descr, color=self.ERRORCOLOR)
			return (1,embObj)
		else:
			self.dbhandler.add_meme(uid=message.author.id, img_url=img_url, caption=caption, template_name=template_name)
			embObj = discord.Embed(title="makememe",description="Here's your meme", color = self.NEKOCOLOR, url=post_url)
			embObj.set_image(url=img_url)
			return (0,embObj)

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
	async def msgarchive(self,message:discord.Message)-> tuple:
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
		nsfw = int(self.dbhandler.get_from_misc("nsfw"))!=0 or type(message.channel)==discord.channel.DMChannel
		link = ""
		error = 0
		img_id = -1
		sigma = int(self.dbhandler.get_from_misc("blur_sigma"))
		if len(args)>1 and args[1].isnumeric and user_pl>self.dbhandler.get_cmd_perm("nhentai"):
			img_id = args[1]
			link = self.dbhandler.get_nhentai_path_by_id(img_id,ignore_block=nsfw)[0]
			if link == -1:
				link = self.nh_handler.get_img(sigma,img_id)
		else:
			sigma = int(self.dbhandler.get_from_misc("blur_sigma"))
			link = self.nh_handler.get_img(sigma)
		if(error==0):
			if nsfw:
				link = f"{link.rstrip('.blurred.jpg')}.jpg"
			img_id = link.rstrip(".blurred.jpg")
			embObj = discord.Embed(title="nHentai Random Cover",description=img_id,color = self.NEKOCOLOR, url=f"https://nhentai.net/g/{img_id.lstrip('nhentai/')}")
			try:
				file_to_send = discord.File(link,filename="SPOILER_FILE.jpg",spoiler=True)
			except FileNotFoundError: #accidentally pushed dumb shit; this will rarely occur but prolly fixes it
				link2 = link.rstrip(".blurred.jpg")+".jpg"
				#print("[commandhandler.py] nh command; lin2 in catch block = ",link2)

				self.nh_handler._blur(link2,sigma)
				file_to_send = discord.File(link,filename="SPOILER_FILE.jpg",spoiler=True)
			embObj.set_image(url="attachment://SPOILER_FILE.jpg")
		nh_log = open("nhentai/log.txt","a")
		nh_log.write(f">Sent nhentai/{str(img_id).lstrip('nhentai/')}\n")
		nh_log.close()
		return (0,embObj,file_to_send)
	async def nhentaiblock(self,message:discord.Message)->tuple:
		args = message.content[1:].replace("  "," ").split(" ")
		if len(args)>1 and args[1].isnumeric:
			error = self.nh_handler.nhentai_block(args[1])
		else:
			error =3
		return (error,None)
	async def nhentailog(self,message:discord.Message)->tuple:
		try:
			log_len = min(int(self.dbhandler.get_from_misc("nh_log_len")),48)
			with open("nhentai/log.txt")as log_file:
				log_lines = log_file.readlines()
			embObj = discord.Embed(title="nhentai log",color=self.NEKOCOLOR)
			field_cont = ""
			for line in log_lines[-log_len:]:
				field_cont+= line
			embObj.add_field(name="Entries",value=field_cont)
			#log management
			if len(log_lines)>500:
				logging.info("trying to rotate nh log")
			#	print("[commandhandler.py] (nhl) trying to rotate log")
				open("nhentai/log.txt.old","w").writelines(log_lines) #lol idk how this is gonna end
				curr_log = open("nhentai/log.txt","w")
				curr_log.write("")
				curr_log.close()
			
			return (0,embObj)
		except Exception as e:
			embObj = discord.Embed(title="nhentai log", description=str(e), color=self.ERRORCOLOR)
			return (1,embObj)
	async def ping(self,message:discord.Message)-> tuple:
		embObj = discord.Embed(title="Ping",description="Pong!", color= self.SYSTEMCOLOR)
		embObj.add_field(name="Ping",value="TBA ms")
		embObj.add_field(name="Latency",value=str(self.client.latency*1000)[:5]+"ms")
		return (0,embObj)
	async def reload(self,message:discord.Message)->tuple:
		embObj = discord.Embed(title="Reloading...",description="let's hope this doesn't fuck anything up...",color=self.SYSTEMCOLOR)
		return (99,embObj)
	async def reloadissues(self,message:discord.Message)->tuple:
		try:
			ls = issues.getIssues()
			if ls[0][0] == -1:
				error = 1
			else:
				self.dbhandler._execComm("DELETE FROM issues")
				for issue in ls:
					self.dbhandler.addIssue(issue)
				
			embObj = discord.Embed(title="Issues",description="Issues reloaded",color=self.ISSUECOLOR)
			return (0,embObj)
		except Exception as e:
			embObj = discord.Embed(title="Issues",description=str(e), color=self.ERRORCOLOR)
			return	(1,embObj)
	async def say(self,message:discord.Message)-> tuple:
		channel = message.channel
		args = message.content[1:].split(" ")
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
		return (error,None)
	async def setcache(self,message:discord.Message)->tuple:
		args = message.content[1:].split(" ")
		cachelen = args[1]

		try:
			newLen = int(cachelen)
			newLen = self.msgs.set_len(newLen)
			embObj = discord.Embed(title="Tracker",description=f"updated cache length to {newLen}",color=self.TRACKERCOLOR)
			return (0, embObj)
		except Exception as e:
			embObj = discord.Embed(title="Tracker", description=str(e), color=self.ERRORCOLOR)
			return (1,embObj)
	async def setchangelog(self,message:discord.Message)->tuple:
		try:
			args = message.content[1:].split(" ")
			new_changelog = args[1].replace("_"," ")
			self.dbhandler.set_to_misc("changelog",new_changelog)
			return (0,None)
		except Exception as e:
			embObj = discord.Embed(title="setchangelog",description=str(e), color=self.ERRORCOLOR)
			logging.error("Something got fucked up when handling setchangelog")
			#print("[commandhandler.py] UWU SHIT GONE WRONG IN SCL HANDLING")
			return (1, embObj)
	async def setperm(self,message:discord.Message)->tuple:
		own_perm_lev = self.dbhandler.get_perm_level(message.author.id)
		user = message.mentions[0]
		args = message.content[1:].replace("  "," ").split(" ")
		perm_lev = args[2]
		if(int(perm_lev)>=own_perm_lev):
			embObj = discord.Embed(title="setperm", description="Can't set others permission >= your own", color=self.ERRORCOLOR)
			error = 3 #make sure you cant promote yourself or anyone else over your own rank	
		else:
			try:
				error = self.dbhandler.set_perm(user, newpermlev=perm_lev)
				embObj = discord.Embed(title="setperm", description=f"{user.nick} now has permission level {perm_lev}", color=self.SYSTEMCOLOR)
			except Exception as e:
				error = 1
				embObj = discord.Embed(title="setperm", description=str(e), color=self.ERRORCOLOR)
		return (error, embObj)
	async def setstatus(self, message:discord.Message)->tuple:
		try:
			cont = message.content
			args = cont[1:].split(" ")
			type = 1
			error = 0
			splitbyquot = cont.split("\"")
			if(len(splitbyquot) not in (2,3)):
				if len(args)<2:
					return (3,None) #u fucked up
				else:
					stringarg = args[1]
				if(len(args)>2 and args[2].isnumeric()):
					type = args[2]
			else:
				stringarg = splitbyquot[1]
				if(len(splitbyquot)==3 and splitbyquot[2].strip().isnumeric()):
					type = int(splitbyquot[2])
			await self.client.change_presence(activity=discord.Activity(name=stringarg,type= type))
			return (0,None)
		except Exception as e:
			embObj = discord.Embed(title="setstatus", description=str(e), color =self.ERRORCOLOR)
			return (1,embObj)
	async def settrack(self,message:discord.Message)->int:
		try:
			user = message.mentions[0]
			self.toTrackID = user.id
			self.toTrackName = user.mention
			self.msgs.set_user(self.toTrackName)
			embObj = discord.Embed(title="Tracker",description=f"updated tracked user to {self.toTrackName}",color = self.TRACKERCOLOR)
			return (0,embObj)
		except Exception as e:
			embObj = discord.Embed(title="Settrack", description=str(e), color=self.ERRORCOLOR)
			return (1,embObj)
	async def setversion(self,message)-> tuple:
		try:
			args = message.content[1:].split(" ")
			version = args[1]
			self.dbhandler.set_to_misc("version",version)
			embObj = discord.Embed(title="setversion", description= f"Version is now set to {version}", color=self.SYSTEMCOLOR)
			return (0,embObj)
		except Exception as e:
			embObj = discord.Embed(title="setversion", description=str(e), color =self.ERRORCOLOR)
			return (1,embObj)
	async def showissues(self,message:discord.Message) -> tuple:
		try:
			res = self.dbhandler._execComm("select * from issues",True)
			embObj = discord.Embed(title="Issues",color=self.ISSUECOLOR)
			for id,title in res:
				embObj.add_field(name=id,value=title,inline=False)
			return (0,embObj)
		except Exception as e:
			embObj = discord.Embed(title="Issues", description=str(e), color=self.ERRORCOLOR)
			return (1,embObj)
	async def showsourcecode(self,message:discord.Message)->tuple:
		args = message.content[1:].split(" ")
		if len(args)<2:
			embObj = discord.Embed(title="showsourcecode",description="Missing argument, use one of the following")
			val_string = ""
			for fname in self.ALLOWEDSOURCEFILES.keys(): val_string+= fname+", "
			embObj.add_field(name="Files available for display", value = val_string)			
			return (3, embObj)
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
					while line_indx<num_lines and len(msg+lines[line_indx])<1930:
						msg+= f"{str(line_indx+1).rjust(3)}| {lines[line_indx]}\n"
						line_indx+=1
					msg += "\n"+"`"*3
					msg+=f"> Answering to {message.author.nick}"
					return (0, msg)
			else:
				return (4, None)		
	async def source(self,message:discord.Message)->tuple:
		return (0, discord.Embed(
						title="Source",
						description="http://brrr.nighmared.tech",
						color= self.SYSTEMCOLOR))
	async def stalk(self, message:discord.Message)->tuple:
		try:
			args = message.content[1:].split(" ")
			target_id = args[1]
			target_user = await self.client.fetch_user(target_id)
			embObj = discord.Embed(title="Stalking", description =f"Info about {target_user.mention}", color = self.TRACKERCOLOR)
			embObj.add_field(name="Username",value=f"{target_user.name}#{target_user.discriminator}")
			embObj.add_field(name="UID", value=target_user.id)
			embObj.add_field(name="Joined", value=target_user.created_at)
			embObj.set_image(url=target_user.avatar_url)
			return (0, embObj)
		except Exception as e:
			embObj = discord.Embed(title="Stalking", description = str(e), color =self.ERRORCOLOR)
			return (1,embObj)
	async def superdelete(self,message : discord.Message)->tuple:
		target_msg = await message.channel.fetch_message(message.reference.message_id)
		embObj = None
		try:
			await target_msg.delete()
			error = 0
		except discord.Forbidden:
			error = 4
		except discord.NotFound:
			error = 2
		except discord.HTTPException:
			error = 1
		except Exception as e:
			embObj = discord.Embed(title="Superdelete", description=str(e), color=self.ERRORCOLOR)
		return (error,None)
	async def togglecmd(self,message:discord.Message)->tuple:
		try:
			args =message.content[1:].split(" ")
			if args[1].strip() == "?":
				totogglecmd = "help"
			else: 
				totogglecmd = ""
				totogglecmd = self.dbhandler.find_alias(args[1].strip())
			if totogglecmd.strip() == "":
				return (3,None)
			self.dbhandler._execComm(f'''UPDATE commands SET enabled={(1,0)[self.dbhandler.cmd_is_enabled(totogglecmd)]} WHERE cmdname=="{totogglecmd}"''')
			return (0,None)
		except IndexError:
			embObj = discord.Embed(title="togglecmd", description=f"Usage: {self.PREFIX}togglecmd <cmdname>", color=self.ERRORCOLOR)
			return (3,embObj)
		except Exception as e:
			embObj = discord.Embed(title="togglecmd", description=str(e), color = self.ERRORCOLOR)
			return (1,embObj)
	async def togglensfw(self,message:discord.Message)->tuple:
		try:
			new_state = self.dbhandler.toggle_nsfw()
			embObj = discord.Embed(title="Toggled NSFW",color=self.NEKOCOLOR,description=f"Turned explicit content {('off','on')[new_state]}")
			return (0, embObj)
		except OperationalError:
			embObj = discord.Embed(title="togglensfw", description = "-- Something wrong with DB --", color=self.ERRORCOLOR)
			return (1,embObj)
		except Exception as e:
			embObj = discord.Embed(title="togglensfw", description=str(e), color =self.ERRORCOLOR)
			return (1,embObj)
	async def triggerannoy(self,message:discord.Message)->tuple:
		try:
			self.dbhandler.set_to_misc("annoyreaction", (not self.dbhandler.shouldAnnoy()))
			embObj = discord.Embed(title="Tracker", description=f" Turned reaction annoyance {('Off','On')[self.dbhandler.shouldAnnoy()]}",color = self.TRACKERCOLOR)
			return (0,embObj)
		except Exception as e:
			embObj = discord.Embed(title="triggerannoy", description=str(e), color =self.ERRORCOLOR)
			return (1,embObj)
