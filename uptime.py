from datetime import datetime as dt
import logging

IMPORTS = ()
logger = logging.getLogger("botlogger")

class uptime:
	def __init__(self,starttime):
		self.start = starttime
	

	def getUptime(self):
		curr = dt.now()
		diff = curr-self.start
		secs = diff.seconds
		mins = int(secs/60)
		hours = int(mins/60)
		days = diff.days
		years = int(days/365)
		secs %= 60
		mins %= 60
		hours %= 24
		days %= 365
		out = ""

		if years>0 :
			out+= f"{years} Year"+(" ","s ")[years>1]
		if days>0 :
			out+= f"{days} Day"+(" ","s ")[days>1]
		if hours>0 :
			out+= f"{hours} Hour"+(" ","s ")[hours>1]
		if mins>0 :
			out+= f"{mins} Minute"+(" ","s ")[mins>1]
		if days<1 and secs>0 :
			out+= f"{secs} Second"+("","s")[secs>1]
		return out
	

	def get_now_utc(self): #dumb wrapper function so i dont have to import datetime separately in commandhandler
		return dt.utcnow()

def get_now_utc():
	return dt.utcnow()