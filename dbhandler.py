import sqlite3 as sql
class dbhandler:
	def __init__(self,filename):
		self.conn = sql.connect(filename)
		self.cursor = self.conn.cursor()
	
	def get_perm_level(self,uid):
		self.cursor.execute(f'''SELECT permlevel from users where uid=={uid};''')
		try:
			res = self.cursor.fetchall()[0][0]
		except IndexError:
			#print(self.cursor.fetchall())
			res = 0 # no entry for uid
		
		return res

	def add_user(self,uid:int, name:str, permlev:int):

		print(f'''INSERT INTO users(uid, permlevel, name) VALUES({uid},{permlev},"{name}")''')
		self.cursor.execute(f'''INSERT INTO users(uid, permlevel, name) VALUES("{uid}","{permlev}","{name}")''')
		self.conn.commit()
		return 0
	
	def set_perm(self,user, newpermlev):
		#first check if user exists
		uid = user.id
		name = user.mention
		self.cursor.execute(f'''SELECT * FROM users WHERE uid="{uid}"''')
		exists = len(self.cursor.fetchall()) != 0
		if(exists):
			self.cursor.execute(f'''UPDATE users SET permlevel = "{newpermlev}" WHERE uid=="{uid}''')
		else:
			self.add_user(uid,name,newpermlev)
		self.conn.commit()
	
	def get_cmd_perm(self,cmd):
		try:
			print(f'''SELECT permlevel FROM commands WHERE cmdname=={cmd} ''')
			self.cursor.execute(f'''SELECT permlevel FROM commands WHERE cmdname=="{cmd}" ''')	
			res = self.cursor.fetchall()[0][0]
		except Exception:
			print("frick cmd not added")
			res = 4
		return res
	
	def _execComm(self,command:str):
		self.cursor.execute(command)
		self.conn.commit()
		res = self.cursor.fetchall()
		if len(res)>0:
			return res
		else: return -10
