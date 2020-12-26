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

	def add_user(self,uid:int, name:str, permlev:int = 0):
		try:
			self.cursor.execute(f'''INSERT INTO users(uid, permlevel, name) VALUES({uid},{permlev},{name}''')
			return 0
		except:
			return 1
	
	def set_perm(self,user, newpermlev):
		#first check if user exists
		uid = user.id
		name = user.mention
		self.cursor.execute(f"SELECT * FROM users WHERE uid={uid}")
		exists = len(self.cursor.fetchall()) != 0
		if(exists):
			self.cursor.execute(f'''UPDATE users SET permlevel = {newpermlev} WHERE uid=={uid}''')
		else:
			self.add_user(uid,name,newpermlev)
	
	def get_cmd_perm(self,cmd):
		self.cursor.execute(f'''SELECT permlevel FROM commands WHERE cmdname=={cmd.strip()} ''')
		try:
			res = self.cursor.fetchall()[0][0]
		except IndexError:
			print("wtf???")
			res = 4
		return res
		
