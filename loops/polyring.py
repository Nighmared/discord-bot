import logging
import discord
import discord.ext.commands
from discord.ext import tasks
from requests.api import post
import dbhandler
import requests
import xml.etree.ElementTree as ET

IMPORTS = (dbhandler,)
logger = logging.getLogger("botlogger")

POLYRING_CHANNELS = (833645549742981190,)
POLYRING_COLOR = 0x1F407A

class PolyringFetcher(discord.ext.commands.Cog):
	def __init__(self, client:discord.ext.commands.Bot, handler_ref):
		self.client = client
		self.dbhandler = handler_ref.db
		self.handler_ref = handler_ref

		self.getnews.start()
	
	@tasks.loop(seconds=120)
	async def getnews(self):
		if self.handler_ref.ISRELOADING: #dont fuck around during reload
			return;
		feeds = self.dbhandler.get_polyring_feeds()
		posts = self.dbhandler.get_polyring_posts()
		postmap = self.get_post_map(posts)
		stuff_to_send = self.filter_new_posts(feeds,postmap)
		for fid,post in stuff_to_send:
			await self.send_new_post(post)
			self.dbhandler.add_polyring_post(post=post,fid=fid)

	
	def get_post_map(self,posts)->dict:
		pmap = {}
		for post in posts:
			pmap[self.make_post_hash(post)] = post
		return pmap


	def filter_new_posts(self,feeds,postmap):
		header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0',
              'Accept': 'text/html',
              'Accept-Language': 'en-US'}
		new_posts = []
		for fid,f_url,author in feeds:
			print(f_url)
			try:
				xml_root = ET.fromstring(requests.get(url=f_url.strip(),headers=header).content.strip())
			except Exception as e:
				
				logger.fatal(str(e))
				logger.warn(f"Skipping {author}  because of above error, url= {f_url}, status = {requests.get(url=f_url, headers =header).status_code}")
				continue

			dumbfuckingjekyll = False
			if xml_root.find("channel") is None:
				dumbfuckingjekyll = True
		#	print("polyring.py:==> ",author," blog is jekyll?",dumbfuckingjekyll) #TODO remove print

			if dumbfuckingjekyll:
				xml_root = self.__fix_jekyll(xml_root)
			
			#here  we have xml root, and all tags should have their actual name, `dumbfuckingjekyll` also provides info on what structure to expect

			if dumbfuckingjekyll:
				feed_posts = xml_root.findall("entry")
			else:
				feed_posts = xml_root.find("channel").findall("item")
			
			if len(feed_posts)==0:
				logging.warn("no posts found for "+author+"! skipping this feed")
				continue
			
			date_key = ("pubDate","published")[dumbfuckingjekyll]
			desc_key = ("description","summary")[dumbfuckingjekyll]
			for fp in feed_posts:
				if dumbfuckingjekyll:
					fp = self.__fix_jekyll(fp)
				pub = fp.find(date_key).text
				title = fp.find("title").text
				link = fp.find("link")
				if dumbfuckingjekyll:
					link = link.attrib["href"]
				else:
					link = link.text
				try: 
					desc = fp.find(desc_key).text[:40]+"..."
				except AttributeError: #ignore fucky feeds
					logger.error(f"Something wrong with feed {author}, skipping")
					continue;

				post = Post(title,descr=desc,author=author,link=link,pubdate=pub)
				if self.make_post_hash(post.tuple) not in postmap.keys():
					logging.info(f"adding new post by {author}")
					new_posts.append((fid,post))
		return new_posts

	def make_post_hash(self,post_tup:tuple) -> int:
		pub,link,author = post_tup[2:]
		return hash(f".{author}.{link}.{pub}.")

	def __fix_jekyll(self,xml_root):
		for elem in xml_root:
			elem.tag = elem.tag.split("}")[-1] #fix stupid tagnames ffs
		return xml_root

	async def send_new_post(self,post):
		for channel_id in POLYRING_CHANNELS:
			discord_chan = await self.client.fetch_channel(channel_id)
			logging.debug("fetched polyring channel:"+str(discord_chan))
			await discord_chan.send(embed = post.embed() )	 #FIXME uncomment after actually implementing lol






class Post:
	def __init__(
		self,
		title:str,
		descr:str,
		author:str,
		link:str,
		pubdate:str,
	):
		self.title = title
		self.descr = descr
		self.author = author
		if not (link.startswith("http") or link.startswith("https")):
			link = "http://"+link
		self.link = link
		self.pubdate = pubdate
		self.tuple = (self.title, self.descr, self.pubdate, self.link, self.author)


	def embed(self):
		embObj = discord.Embed(title=self.title,description=self.descr,color= POLYRING_COLOR, url=self.link)
		
		embObj.set_author(name=self.author)
		
		return embObj




def update_feeds()->list:
	data = requests.get(url="https://xyquadrat.ch/polyring/data/members.json").json()
	return data