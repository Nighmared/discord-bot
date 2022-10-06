import logging
import socket
import xml.etree.ElementTree as ET
from html import unescape
from time import sleep, time

import discord
import discord.ext.commands
import requests
from discord.errors import Forbidden, HTTPException
from discord.ext import tasks
from requests.exceptions import Timeout

import dbhandler

IMPORTS = (dbhandler,)
logger = logging.getLogger("botlogger")

POLYRING_CHANNELS = (833645549742981190,)
POLYRING_COLOR = 0x1F407A

# increase default socket timeout
socket.setdefaulttimeout(10)


class Post:
    def __init__(
        self,
        title: str,
        descr: str,
        author: str,
        link: str,
        pubdate: str,
        guid: str,
    ):
        self.title = title
        self.descr = descr
        self.author = author
        if not (link.startswith("http") or link.startswith("https")):
            link = "http://" + link
        self.link = link
        self.pubdate = pubdate
        if not guid.startswith("http"):
            guid = "http://" + guid
        self.guid = guid
        self.tuple = (self.title, self.descr, self.pubdate, self.link, self.author)
        self.post_id = -1

    def embed(self):
        embObj = discord.Embed(
            title=self.title,
            description=self.descr,
            color=POLYRING_COLOR,
            url=self.guid,
        )
        embObj.set_author(name=self.author)
        return embObj


class PolyringFetcher(discord.ext.commands.Cog):
    def __init__(self, client: discord.ext.commands.Bot, handler_ref):
        self.client = client
        self.dbhandler: dbhandler.Dbhandler = dbhandler.Dbhandler("discordbot.db")
        self.handler_ref = handler_ref
        self.getnews.start()

    @tasks.loop(minutes=5)
    async def getnews(self):
        if not self.dbhandler:
            return

        if self.handler_ref.ISRELOADING:  # dont fuck around during reload
            return
        try:
            if (
                int(self.dbhandler.get_from_misc("debug")) > 0
            ):  # dont send polyring posts on debug deploy...
                return
        except Exception:
            logger.error("db error")
            sleep(2)
            if int(self.dbhandler.get_from_misc("debug")) > 0:
                return

        feeds: tuple[int, str, str] = self.dbhandler.get_polyring_feeds()
        posts: list[Post] = self.dbhandler.get_polyring_posts()
        post_guid_set = self.get_post_guid_set(posts)
        stuff_to_send = self.filter_new_posts(feeds, post_guid_set)
        for fid, post in stuff_to_send:
            new_pid = self.dbhandler.add_polyring_post(post=post, fid=fid)
            post.post_id = new_pid
            await self.send_new_post(post)
        self.dbhandler.ping_loop("Polyring", time())

    def get_post_guid_set(self, posts) -> dict:
        res = set()
        for post in posts:
            guid = post[5]
            res.add(guid)
        return res

    def filter_new_posts(self, feeds, post_guid_set) -> list[tuple[int, Post]]:
        header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0",
            "Accept": "text/html",
            "Accept-Language": "en-US",
        }
        new_posts: list[tuple[int, Post]] = []
        for fid, f_url, author in feeds:
            # print(f_url)
            try:
                resp = requests.get(url=f_url.strip(), headers=header, timeout=10)
                xml_root = ET.fromstring(resp.content.strip())

            except ET.ParseError:
                logger.error(
                    "Got error when trying to parse XML response from %ss feed. Url: %s",
                    author,
                    f_url.strip(),
                    exc_info=1,
                )
                continue
            except socket.timeout:
                logger.error(
                    "Got socket timeout error when receiving results from %s [Feed author: %s]. Skipping",
                    f_url.strip(),
                    author,
                )
                continue
            except Timeout:
                logger.error("Timed out trying to fetch feed of %s. Skipping.", author)
                continue

            except requests.exceptions.RequestException:
                logger.error(
                    "Got unhandled exception from request when trying to fetch %ss feed. Skipping.",
                    author,
                    exc_info=1,
                )
                continue

            except Exception:
                logger.fatal("Got error when trying to fetch feed", exc_info=1)
                logger.warning(
                    "Skipping %s  because of above error, url=%s, status = %i",
                    author,
                    f_url,
                    resp.status_code,
                )
                continue
            dumbfuckingjekyll = xml_root.find("channel") is None

            if dumbfuckingjekyll:
                xml_root = self.__fix_jekyll(xml_root)

            # here we have xml root, and all tags should have their
            # actual name, `dumbfuckingjekyll` also provides info on
            # what structure to expect

            if dumbfuckingjekyll:
                feed_posts = xml_root.findall("entry")
            else:
                feed_posts = xml_root.find("channel").findall("item")

            if feed_posts is None:
                logger.fatal("%s has weird feed. <3", author, exc_info=1)
                continue

            if len(feed_posts) == 0:
                logger.warning("no posts found for %s! skipping this feed", author)
                continue

            date_key = ("pubDate", "published")[dumbfuckingjekyll]
            desc_key = ("description", "summary")[dumbfuckingjekyll]
            guid_key = ("guid", "id")[dumbfuckingjekyll]
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
                guid_res = fp.find(guid_key)
                if guid_res is None:
                    # yet another generator??
                    # check for B!Soft used by Solitude
                    logger.debug(
                        "Couldn't find guid for post on %s. Using <link> as guid instead",
                        f_url,
                    )
                    guid_res = link

                    generator_res = xml_root.find("channel").find("generator")
                    if generator_res is not None:
                        if "B!Soft" in generator_res.text:
                            desc_key = "description"
                    else:
                        logger.fatal(
                            "No idea whats wrong with this feed.. Author: %s, feed: %s",
                            author,
                            f_url,
                        )

                else:
                    guid_res = guid_res.text

                # for some reason its possible for some rss values to start with
                # "tag:" :reeeeee:
                guid = guid_res.strip().lstrip("tag:")
                try:
                    desc = unescape(fp.find(desc_key).text[:40] + "...")
                except (TypeError, AttributeError):  # ignore fucky feeds
                    try:
                        desc = unescape(
                            fp.find(("summary", "description")[dumbfuckingjekyll]).text[
                                :40
                            ]
                            + "..."
                        )
                    except (TypeError, AttributeError):
                        desc = "[No description tag provided]"
                post = Post(
                    title, descr=desc, author=author, link=link, pubdate=pub, guid=guid
                )
                if post.guid not in post_guid_set:
                    logger.info("adding new post by %s", author)
                    new_posts.append((fid, post))
        if len(new_posts) > 0:
            logger.info(
                "returning from post doing stuff thingy with %i new posts",
                len(new_posts),
            )
        return new_posts

    def __fix_jekyll(self, xml_root):
        for elem in xml_root:
            elem.tag = elem.tag.split("}")[-1]  # fix stupid tagnames ffs
        return xml_root

    async def send_new_post(self, post: Post):
        for channel_id in POLYRING_CHANNELS:
            discord_chan = await self.client.fetch_channel(
                channel_id
            )  # type: discord.TextChannel
            logger.debug("fetched polyring channel: %s", str(discord_chan))
            try:
                msg = await discord_chan.send(embed=post.embed())
                await msg.add_reaction("<:yay:853288251325153320>")
            except Forbidden:
                if channel_id == 833645549742981190:
                    logger.fatal(
                        "Got Forbidden when trying to post a new polyring post. time to ping lukas!"
                    )
                    spam_chan = await self.client.fetch_channel(768600365602963496)
                    await spam_chan.send(
                        content="<@!223932775474921472> BRUH GIB PERMS FOR POLYRING"
                    )
                else:
                    logger.fatal(
                        "Got forbidden when trying to send polyring posts. channel id: %i",
                        channel_id,
                    )
                continue
            except HTTPException as error:

                if error.code == 50035:
                    # discord error code for invalid form body
                    # is probably misformed url
                    logger.warning(
                        "Polyring post with id %i could"
                        "not be sent because the url is probably bad. Will be ignored!",
                        post.post_id,
                    )
                else:
                    # if not something specifically handled, just
                    # pass on
                    raise error

    def cog_unload(self):
        self.dbhandler.close_down()
        self.getnews.stop()
        super.cog_unload()


def update_feeds() -> list:
    data = requests.get(url="https://xyquadrat.ch/polyring/data/members.json").json()
    return data
