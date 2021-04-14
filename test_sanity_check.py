from random import random
from re import A
import requests
from sys import stdout
from datetime import datetime
from time import sleep



XKCD_NUM_LIMIT = 2000

RH_STRINGLEN_LIMIT = 30




def test_imports_tuples():
	import msghandler as msgh # same as above
	print("sdf\n")
	print("\033[0;32m")
	for impo in msgh.IMPORTS:
		if type(impo.IMPORTS) != tuple: # make sure that all modules have an IMPORTS tuple defined, otherwise softreload can break
			print("\033[0;31m",end="")
			print(f"Failed Module: {impo.__name__}")
			print("\033[0m")
			assert False #fail
		else:
			print(f"Valid Module: {impo.__name__}".ljust(40),end="\n")
		for subimp in impo.IMPORTS:
			if type(subimp.IMPORTS) != tuple: #same but for imports of the imported modules
				print("\033[0;31m",end="")
				print(f"Failed Module: {subimp.__name__}".ljust(40))
				print("\033[0m",end="")
				assert False #fail it here
			else:
				print(f"Valid Module: {subimp.__name__}".ljust(40))


	print("\033[0m")
	print("\n\n")

class Test_APIs:
	def test_xkcd(self): #run example xkcd call to make sure json structure is still okay
		import xkcd
		res = xkcd.get_latest()
		assert res["success"] == True
		res = xkcd.get_comic(int(random()*XKCD_NUM_LIMIT))
		assert res["success"] == True

	def test_robohash(self): #-...
		import robohash
		dummy_string_len = int(random()*RH_STRINGLEN_LIMIT+10)
		dummy_string = ""
		for i in range(dummy_string_len):
			dummy_string += chr(97+int(random()*26))

		res = robohash.get_embed(dummy_string) # check that it doesnt fail

	def test_issues(self):
		import issues
		res = issues.getIssues()
		assert issues != (-1,-1)
	
	def test_inspiro(self):
		import inspirobot
		res = inspirobot.get_img_url()
		assert res[0] == False #first element is boolean error flag
	
	def test_uptime(self):
		import uptime
		a_time = datetime.now()
		tracker = uptime.uptime(a_time)
		sleep(1)
		res_string = tracker.getUptime()
		print(res_string)
		assert "Second" in res_string
		assert ("Seconds" in res_string) == False
		assert ("Year" in res_string) == False
		assert ("Day" in res_string) == False
		assert ("Hour" in res_string) == False
		assert ("Minute" in res_string) == False
		sleep(3)
		res_string = tracker.getUptime()
		assert "Seconds" in res_string
		assert ("Second " in res_string) == False
		assert ("Year" in res_string) == False
		assert ("Day" in res_string) == False
		assert ("Hour" in res_string) == False
		assert ("Minute" in res_string) == False

class Test_Invalid_Input:
	def test_robohash(self):
		import robohash
		res = robohash.get_embed("")

	def test_xkcd(self):
		import xkcd
		res = xkcd.get_comic(-1)
		assert res["success"] == False

class Tests_Slow_Cases:
	def test_shorten(self): # same as for xkcd
		import shorten
		res = shorten.shorten_link("ethz.wtf")
		assert res[0] == 0 # no error

	def test_shorten_invalid(self):
		import shorten
		res = shorten.shorten_link(-1)
		assert res[0] != 0
		res = shorten.shorten_link("")
		assert res[0] != 0
	

#this one is probably redundant.. but still
def test_import_all():
	import discord
	import bot
	import commandhandler
	import dbhandler
	import inspirobot
	import issues
	import meme
	import msghandler
	import msglist
	import neko
	import nhentai
	import robohash
	import stalk
	import uptime
	import xkcd
