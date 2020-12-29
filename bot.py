from logging import error
from re import split
import discord
import msglist
import dbhandler
import commandhandler
from sys import exit


SUDOID = 291291715598286848
TOKEN = open(".token.txt").read()
PREFIX = "°"
msgs = msglist.msglist(5)
client = discord.Client()
db = dbhandler.dbhandler("discordbot.db")
handler = commandhandler.commandhandler(dbhandler=db,msgs=msgs,PREFIX=PREFIX,client=client)



#EMOJIS
pepelove = "<:pepelove:778369435244429344>"
pepegun = "<:pepegun:747783377716904008>"
confusedcat = "<:confusedcat:771041402930987068>"
hm = "<:hm:779012743583498240>"
cope = "<:wojak_cope:767839352255676417>"
c_yfu = "<:code_youfuckedup:785435875030728724>"
hahaa = "<:haHaa:747783377536680066>"
########




addedEmotesToHelp = False


reaction_text_dict = {
	0:"Everything gud",
	1:"nono thats not how its supposed to go",
	2:"Nothing to display",
	3:"You fucked up ur command mister",
	4:"Not enough permissions",
	5:"All fine but bot can't text here... F",
}



def perm_valid(cmd:str,permlevel:int) -> bool:
	return permlevel>= db.get_cmd_perm(cmd)



async def add_reaction(message, emote):
	try:
		await message.add_reaction(emote)
		return 0
	except discord.errors.Forbidden:
		return 5

@client.event
async def on_ready():
	print(f'{client.user} has connected')

@client.event
async def on_message(message:discord.message):
	global addedEmotesToHelp

	#block bots
	if(message.author.bot):
		return

	#allow only one server
#	if(message.guild.id != ALLOWEDGUILD):return
	
	isCommand = message.content.startswith(PREFIX)
	permlevel = db.get_perm_level(message.author.id)
	isJoniii = message.author.id == SUDOID #hardcode that sucker
	if(isJoniii): permlevel = 5
	cmd = db.find_alias(message.content[1:].split(" ")[0].lower())


	error_dict = {
		0 : pepelove, #success
		1 : pepegun, #invalid stuff
		2 : hm, # no msgs to display
		3 : c_yfu, # wrong args
		4 : cope, #perms
		5 : hahaa, #bot cant send here D;
	}
	if(int(db.get_from_misc("standby")) == 1  and not cmd == "deepsleep"): #ignore everything in standby
		return


	if(message.author.id == handler.toTrackID and not isCommand):
		#print(message.content)
		msgs.add_msg(message)
		if(db.shouldAnnoy()): await add_reaction( message,confusedcat)

	if(isCommand):
	#	if(len(last_MSG)>0 and len(last_MSG[-1].embeds[0])>int(handler.get_from_misc("max_perm_msg_len"))):
	#		await last_MSG.pop().delete()
		if not perm_valid(cmd,permlevel):
			res = 4
		else:
			res = await handler(message,permlevel)
		if(res == 99): #RELOAD
			exit(0)
		await add_reaction( message,error_dict[res])
		await message.delete(delay=3)
		
		

client.run(TOKEN)
