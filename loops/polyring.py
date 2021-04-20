import logging
import discord
import discord.ext.commands
from discord.ext import tasks
import dbhandler


IMPORTS = (dbhandler,)
logger = logging.getLogger("botlogger")

POLYRING_CHANNELS = (833645549742981190,)
POLYRING_COLOR = 0x00FFFF

class PolyringFetcher(discord.ext.commands.Cog):
	def __init__(self, client:discord.ext.commands.Bot,dbhandler:dbhandler.Dbhandler):
		self.client = client
		self.dbhandler = dbhandler
		self.getnews.start()
	
	@tasks.loop(seconds=10)
	async def getnews(self):
		#FIXME implement this
		post = Post("NEW FEATURE COMING SOON",descr="but not yet working",author="joniii",link="https://blog.ethz.wtf")	
		await self.send_new_post(post)

	async def send_new_post(self,post):
		for channel_id in POLYRING_CHANNELS:
			discord_chan = await self.client.fetch_channel(channel_id)
			logging.debug("fetched polyring channel:"+str(discord_chan))
			#await discord_chan.send(embed = post.embed() )	 #FIXME uncomment after actually implementing lol






class Post:
	def __init__(
		self,
		title:str,
		descr:str,
		author:str,
		link:str,
	):
		self.title = title
		self.descr = descr
		self.author = author
		self.link = link

	
	def embed(self):
		embObj = discord.Embed(title=self.title,description=self.descr,color= POLYRING_COLOR, url=self.link)
		
		embObj.set_author(name=self.author) #TODO add icon_url property by fetching user from db :>
										#TODO new table to link blogs and discord users
		
		return embObj


