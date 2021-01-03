from datetime import datetime as dt
class uptime:
	def __init__(self):
		self.start = dt.now()
	

	def getUptime(self):
		curr = dt.now()
		diff = curr-self.start
		secs = diff.seconds
		mins = int(secs/60)
		hours = int(mins/60)
		days = int(hours/24)
		years = int(days/365)
		secs %= 60
		mins %= 60
		hours %= 24
		days %= 365
		out = ""
		if years>0 :
			out+=years+" Years "
		if days>0 :
			out+=days+" Days "
		if hours>0 :
			out+=hours+" Hours "
		if mins>0 :
			out+=mins+" Minutes "
		if days<1 and secs>0 :
			out+= secs +" Seconds"
		return out