import sqlite3 as sql
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

	def increment_user_message_count(self,uid,name:str):
		self.cursor.execute('''SELECT uid,msgcount FROM users''')
		messagecounts = {}
		for uid,msgcount in self.cursor.fetchall():
			messagecounts[uid] = int(msgcount)
		if(str(uid) in messagecounts.keys()):
			self.cursor.execute(f'''UPDATE users SET msgcount={messagecounts[uid]+1} WHERE uid='{uid}' ''')
		else:
			self.cursor.execute(f'''INSERT INTO users(uid,permlevel,name,msgcount) VALUES({uid},0,'{name}',1)''')
		
	def set_perm(self,user, newpermlev):
		#first check if user exists
		uid = user.id
		name = user.mention
		self.cursor.execute(f'''SELECT * FROM users WHERE uid=={uid}''')
		res = self.cursor.fetchall()
		exists = len(res) != 0
		if(exists):
			self.cursor.execute(f'''UPDATE users SET permlevel = "{newpermlev}" WHERE uid=={uid}''')
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
		print(id)
		self.cursor.execute(f'''SELECT value FROM emotes WHERE id=={id}''')
		res = self.cursor.fetchall()[0][0]
		return res
	
	def create_backup(self):
		backup = sql.connect("backup.db")
		self.conn.backup(backup)
		backup.commit()
		backup.close()
		return 0