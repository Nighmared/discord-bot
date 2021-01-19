import sqlite3 as sql
import subprocess as sub
from datetime import datetime as dt
IMPORTS = () 

class dbhandler:
	def __init__(self,filename):
		self.conn = sql.connect(filename)
		self.cursor = self.conn.cursor()
	
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
		self.cursor.execute('''SELECT uid,msgcount,name FROM users''')
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
			print("[dbhandler.py] (get_cmd_perm) frick cmd not added",cmd)
			res = 4
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
		timestring = str(dt.now().isoformat())[:-7]
		sub.run(["cp","discordbot.db",f"backups/{timestring}.db"])
		print(f"[dbhandler.py](create_backup) Created Backup > {timestring}")
		return 0