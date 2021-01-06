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
		print("[uptime.py debugging]> ",diff,years,days,hours,mins,secs,"  [diff  yrs  days  hours  mins secs]")

		if years>0 :
			out+= f"{years} Years "
		if days>0 :
			out+= f"{days} Days "
		if hours>0 :
			out+= f"{hours} Hours "
		if mins>0 :
			out+= f"{mins} Minutes "
		if days<1 and secs>0 :
			out+= f"{secs} Seconds"
		return out