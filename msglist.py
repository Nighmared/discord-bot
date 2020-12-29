class msglist:
	def __init__(self,maxlen,tracked_user = "nobody"):
		self.maxlen = maxlen
		self.ls = []
		self.uName = tracked_user

	def add_msg(self,msg):
		self.ls.append(msg)
		while(len(self.ls)>self.maxlen):
			self.ls.pop(0)
	def set_len(self,newLen:int):
		newLen = min(max(1,newLen),1000)
		self.maxlen = newLen
		return newLen
	def set_user(self,newName):
		self.uName = newName
		self.ls.clear()
	
	def __repr__(self) -> str:
		while(len(self.ls)>self.maxlen):
			self.ls.pop(0)
		res = ""
		for msg in self.ls:
			res += f"{msg.created_at} {self.uName} > {msg.content[:100]}"
			res+="\n"
		return res
	def sendable(self):
		return self.ls