import sqlite3 as sql
from sqlite3.dbapi2 import OperationalError
import subprocess as sub
import logging
from datetime import datetime as dt
IMPORTS = () 

class dbhandler:
	def __init__(self,filename):
		self.db_fname = filename
		self.conn = sql.connect(filename)
		self.cursor = self.conn.cursor()
		self.cursor.execute('''PRAGMA foreign_keys=ON;''')
	
	def get_perm_level(self,uid):
		self.cursor.execute(f'''SELECT permlevel from users where uid=={uid};''')
		try:
			res = self.cursor.fetchall()[0][0]
		except IndexError:
			res = 0 # no entry for uid
		
		return res

	def add_user(self,uid:int, name:str, permlev:int):

		self.cursor.execute(f'''INSERT INTO users(uid, permlevel, name) VALUES("{uid}","{permlev}","{name}")''')
		self.conn.commit()
		return 0

	def increment_user_message_count(self,author_uid:int,name:str,mention):
		self.cursor.execute('''SELECT uid,msgcount,name FROM users;''')
		uid_dict = {}
		for uid,msgcount,uname in self.cursor.fetchall():
			uid_dict[uid] = (int(msgcount),uname)
		if(author_uid in uid_dict.keys()):
			if(uid_dict[author_uid][1] != mention):
				self.cursor.execute(f'''UPDATE users SET name='{mention}' where uid='{author_uid}' ''')
			self.cursor.execute(f'''UPDATE users SET msgcount={uid_dict[author_uid][0]+1} WHERE uid='{author_uid}' ''')
		else:
			self.cursor.execute(f'''INSERT INTO users(uid,permlevel,name,msgcount) VALUES({author_uid},0,'{mention}',1)''')

	def get_most_messages(self):
		self.cursor.execute('''SELECT name,msgcount FROM users ORDER BY msgcount DESC''')
		res = self.cursor.fetchall()
		return res

	def set_perm(self,user, newpermlev):
		#first check if user exists
		uid = user.id
		name = user.mention
		self.cursor.execute(f'''SELECT * FROM users WHERE uid=={uid}''')
		res = self.cursor.fetchall()
		exists = len(res) != 0
		if(exists):
			self.cursor.execute(f'''UPDATE users SET permlevel = "{newpermlev}" WHERE uid=='{uid}' ''')
		else:
			self.add_user(uid,name,newpermlev)
		self.conn.commit()
	
	def get_cmd_perm(self,cmd):
		try:
			self.cursor.execute(f'''SELECT permlevel FROM commands WHERE cmdname=="{cmd}" ''')	
			res = self.cursor.fetchall()[0][0]
		except Exception:
			#print("[dbhandler.py] (get_cmd_perm) frick cmd not added",cmd)
			logging.warning(f"Unable to look up permission level of {cmd} ")
			res = 8 #return dumb high number as default
		return res

	def get_from_misc(self,key):
		self.cursor.execute(f'''select value from misc where key=="{key}"''')
		return self.cursor.fetchall()[0][0]

	def set_to_misc(self,key,value):
		self.cursor.execute(f'''update misc SET value="{str(value).replace("_"," ")}" where key=="{key}"''')
		self.conn.commit()
	
	def find_alias(self, shortcut:str)->str:
		self.cursor.execute('''select cmdname,alias FROM commands''')# WHERE enabled==1''')
		res = self.cursor.fetchall()
		aliases = {}
		for (cmdname,alias) in res:
			aliases[alias] = cmdname
		
		if shortcut in aliases.keys():
			return aliases[shortcut]
		elif shortcut in aliases.values():
			return shortcut
		else:
			return ""

	def _execComm(self,command:str, raw=False):
		self.cursor.execute(command)
		self.conn.commit()
		res = self.cursor.fetchall()
		if(raw):
			return res
		if len(res)>0:
			out = ""
			for r in res:
				out+= str(r)+"\n"
			return out
		else: return -10
	
	def shouldAnnoy(self)->bool:
		res = self.get_from_misc("annoyreaction")
		
		return(res.strip() == "True")

	def addIssue(self,issueTuple):
		id,title = issueTuple
		self.cursor.execute(f'''SELECT * FROM issues WHERE id=={id}''')
		res = self.cursor.fetchall()
		if(len(res) == 0):
			self.cursor.execute(f'''INSERT INTO issues(id,title) VALUES({id},"{title}")''')
		self.conn.commit()
	
	def fixissue(self,id:int):
		self.cursor.execute(f'''DELETE FROM issues WHERE id=={id}''')

	def cmd_is_enabled(self,cmd:str)->bool:
		self.cursor.execute(f'''select enabled from commands where cmdname=="{cmd}"''')
		try:
			enabled = int(self.cursor.fetchall()[0][0])>0
		except IndexError:
			enabled = False
		return enabled
	
	def get_emote(self,id:int)->str:
		self.cursor.execute(f'''SELECT value FROM emotes WHERE id=={id}''')
		res = self.cursor.fetchall()[0][0]
		return res
	
	def create_backup(self):
		self.set_to_misc("standby",1)
		self.close_down()
		timestring = str(dt.now().isoformat())[:-7]
		sub.run(["cp","discordbot.db",f"backups/{timestring}.db"])
		#print(f"[dbhandler.py](create_backup) Created Backup > {timestring}")
		logging.info(f"Created Backup time: {timestring} ")
		self.conn = sql.connect(self.db_fname)
		self.cursor = self.conn.cursor()
		self.cursor.execute('''PRAGMA foreign_keys = ON;''')
		self.cursor.fetchall()
		self.set_to_misc("standby",0)
		return 0
	
	def add_nhentai_file(self,id,path_to_blurred):
		self.cursor.execute(f'''INSERT INTO nhentai(id, path) VALUES({id},'{path_to_blurred}') ''')
		self.conn.commit()

	def get_nhentai_ids(self):
		self.cursor.execute('''select id from nhentai''')
		res = self.cursor.fetchall()
		return res
	def get_nhentai_path_by_id(self,id,ignore_block = False):
		self.cursor.execute(f'''select path,blocked from nhentai where id={id}''')
		res = self.cursor.fetchall()
		if len(res) == 0:
			res.append((-1,))
		elif res[0][1]==1 and not ignore_block:
			res[0] = (("nhentai/steurer.blurred.jpg",)) #so other stuff still works
		return res[0]
	def get_nhentai_blocked(self)->list:
		self.cursor.execute('''select id from nhentai where blocked=1''')
		res = self.cursor.fetchall()
		if len(res)>0:
			return res[0]
		else:
			return []
	def toggle_nsfw(self)->bool:
		res = self.get_from_misc("nsfw")
		new_val = (1,0)[int(res)]
		self.set_to_misc("nsfw",new_val)
		self.conn.commit()
		return new_val>0
	def nhentai_block(self,id)->None:
		self.cursor.execute(f'''select blocked from nhentai where id={id}''')
		curr_state = self.cursor.fetchall()[0][0]
		self.cursor.execute(f'''UPDATE nhentai SET blocked={1-int(curr_state)} WHERE id={id}''')
		self.conn.commit()

	def add_meme(self, template_name:str, uid:int, caption:str, img_url:str)->int:
		try:
			self.cursor.execute(f'''
			INSERT INTO generated_memes(template_name, user, caption, img_url)
			VALUES ("{template_name}", {uid}, "{caption}", '{img_url.strip()}')''')
			self.conn.commit()
			return 0
		except OperationalError as e:
			print("[dbhandler.py] add_meme got fucked -> ", str(e))

	def get_meme_templates(self)->dict:
		self.cursor.execute('''SELECT template_name,template_id FROM meme_templates''')
		res = self.cursor.fetchall()
		templates = {}
		for name,id in res:
			templates[name] = id
		return templates
	
	def add_meme_template(self,template_name,template_id):
		self.cursor.execute('''INSERT INTO meme_templates(template_name,template_id) VALUES(?,?)''', (template_name,template_id))
		self.conn.commit()

	def close_down(self)->None:
		self.conn.close()