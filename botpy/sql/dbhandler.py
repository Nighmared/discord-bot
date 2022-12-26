import logging
import os
import sqlite3 as sql
import subprocess as sub
from datetime import datetime as dt
from sqlite3.dbapi2 import OperationalError
from typing import Any, Optional, Union

FALLBACK_PREFIX = "°"  # for transition from static prefix, hotfix in case shit fails

logger = logging.getLogger("botlogger")

IMPORTS = ()


class Dbhandler:
    def __init__(self, filename):
        self.db_fname = filename
        self.conn = sql.connect(filename)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""PRAGMA foreign_keys=ON;""")
        no_db = os.environ.get("BOT_NO_DB", default="false") == "true"
        if not no_db and self.get_from_misc("prefix") is None:
            self.set_to_misc("prefix", FALLBACK_PREFIX)  # Failsafe, kinda

    def get_perm_level(self, uid):
        with self.conn:
            self.cursor.execute(f"""SELECT permlevel from users where uid=={uid};""")
            try:
                res = self.cursor.fetchall()[0][0]
            except IndexError:
                res = 0  # no entry for uid

        return res

    def add_user(self, uid: int, name: str, permlev: int):
        with self.conn:
            self.cursor.execute(
                """INSERT INTO users(uid, permlevel, name) VALUES(?,?,?)""",
                (uid, permlev, name),
            )
        return 0

    def increment_user_message_count(self, author_uid: int, name: str, mention):
        with self.conn:
            self.cursor.execute(
                """SELECT uid,msgcount,name,readable_name FROM users;"""
            )
            tmp_res = self.cursor.fetchall()
        uid_dict = {}
        for uid, msgcount, uname, display_name in tmp_res:
            uid_dict[uid] = (int(msgcount), uname, display_name)
        if author_uid in uid_dict.keys():
            if uid_dict[author_uid][1] != mention:
                with self.conn:
                    self.cursor.execute(
                        """UPDATE users SET name=? where uid=? """,
                        (mention, author_uid),
                    )
            if uid_dict[author_uid][2] != name:
                with self.conn:
                    self.cursor.execute(
                        """UPDATE users SET readable_name=? WHERE uid=?""",
                        (name, author_uid),
                    )
                self.cursor.execute(
                    """UPDATE users SET msgcount=? WHERE uid=? """,
                    (uid_dict[author_uid][0] + 1, author_uid),
                )
        else:
            with self.conn:
                self.cursor.execute(
                    "INSERT INTO users(uid,permlevel,name,msgcount,readable_name)"
                    + " VALUES(?,?,?,?,?)",
                    (author_uid, 0, mention, 1, name),
                )

    def get_most_messages(self):
        with self.conn:
            self.cursor.execute(
                """SELECT name,msgcount FROM users ORDER BY msgcount DESC LIMIT 20"""
            )
            res = self.cursor.fetchall()
        return res

    def set_perm(self, user, newpermlev) -> int:
        # first check if user exists
        uid = user.id
        name = user.mention
        with self.conn:
            self.cursor.execute("""SELECT * FROM users WHERE uid==?""", (uid))
            res = self.cursor.fetchall()
        exists = len(res) != 0
        if exists:
            with self.conn:
                self.cursor.execute(
                    """UPDATE users SET permlevel = ? WHERE uid==? """,
                    (newpermlev, uid),
                )
        else:
            self.add_user(uid, name, newpermlev)
        return 0

    def get_cmd_perm(self, cmd: str):
        try:
            with self.conn:
                self.cursor.execute(
                    """SELECT permlevel FROM commands WHERE cmdname==? """, (cmd,)
                )
                res = self.cursor.fetchall()[0][0]
        except Exception:
            # print("[dbhandler.py] (get_cmd_perm) frick cmd not added",cmd)
            logger.warning("Unable to look up permission level of %s ", cmd)
            res = 8  # return dumb high number as default
        return res

    def get_from_misc(self, key) -> str:
        with self.conn:
            self.cursor.execute("""select value from misc where key==?""", (key,))
            try:
                return self.cursor.fetchall()[0][0]
            except IndexError:
                return ""

    def set_to_misc(self, key, value):
        with self.conn:
            self.cursor.execute(
                """update misc SET value=? where key==?""",
                (str(value).replace("_", " "), key),
            )

    def find_alias(self, shortcut: str) -> str:
        with self.conn:
            self.cursor.execute(
                """select cmdname,alias FROM commands"""
            )  # WHERE enabled==1''')
            res = self.cursor.fetchall()
        aliases = {}
        for (cmdname, alias) in res:
            aliases[alias] = cmdname

        if shortcut in aliases.keys():
            return aliases[shortcut]
        elif shortcut in aliases.values():
            return shortcut
        else:
            return ""

    def _raw_execComm(self, command) -> list[Any]:
        with self.conn:
            self.cursor.execute(command)
            res = self.cursor.fetchall()
        return res

    def _execComm(self, command: str) -> Union[str, int]:
        res = self._raw_execComm(command)
        if len(res) > 0:
            out = "\n".join(res)
            return out
        else:
            return -10

    def shouldAnnoy(self) -> bool:
        res = self.get_from_misc("annoyreaction")
        return res.strip() == "True"

    def add_issue(self, issue_t):
        issue_id, title, tag_s = issue_t
        with self.conn:
            self.cursor.execute(f"""SELECT * FROM issues WHERE id=={issue_id}""")
        res = self.cursor.fetchall()
        if len(res) == 0:
            with self.conn:
                self.cursor.execute(
                    """INSERT INTO issues(id,title,tags) VALUES(?,?,?)""",
                    (issue_id, title, tag_s),
                )

    def fixissue(self, issue_id: int):
        with self.conn:
            self.cursor.execute("""DELETE FROM issues WHERE id==?""", (issue_id,))

    def cmd_is_enabled(self, cmd: str) -> bool:
        with self.conn:
            self.cursor.execute(
                """select enabled from commands where cmdname==?""", (cmd,)
            )
        try:
            enabled = int(self.cursor.fetchall()[0][0]) > 0
        except IndexError:
            enabled = False
        return enabled

    def get_emote(self, emote_id: int) -> str:
        with self.conn:
            self.cursor.execute("""SELECT value FROM emotes WHERE id==?""", (emote_id,))
            res = self.cursor.fetchall()[0][0]
        return res

    def create_backup(self):
        self.set_to_misc("standby", 1)
        self.close_down()
        timestring = str(dt.now().isoformat())[:-7]
        sub.run(["cp", "discordbot.db", f"backups/{timestring}.db"])
        logger.info(f"Created Backup time: {timestring} ")
        self.conn = sql.connect(self.db_fname)
        self.cursor = self.conn.cursor()
        with self.conn:
            self.cursor.execute("""PRAGMA foreign_keys = ON;""")
            self.cursor.fetchall()
        self.set_to_misc("standby", 0)
        return 0

    def add_nhentai_file(self, nh_id, path_to_blurred):
        with self.conn:
            self.cursor.execute(
                f"""INSERT INTO nhentai(id, path) VALUES({nh_id},'{path_to_blurred}') """
            )

    def get_nhentai_ids(self):
        with self.conn:
            self.cursor.execute("""select id from nhentai""")
            res = self.cursor.fetchall()
        return res

    def get_nhentai_path_by_id(self, nh_id, ignore_block=False):
        with self.conn:
            self.cursor.execute(
                f"""select path,blocked from nhentai where id={nh_id}"""
            )
            res = self.cursor.fetchall()
        if len(res) == 0:
            res.append((-1,))
        elif res[0][1] == 1 and not ignore_block:
            res[0] = ("nhentai/steurer.blurred.jpg",)  # so other stuff still works
        return res[0]

    def get_nhentai_blocked(self) -> list:
        with self.conn:
            self.cursor.execute("""select id from nhentai where blocked=1""")
            res = self.cursor.fetchall()
        if len(res) > 0:
            return res[0]
        else:
            return []

    def toggle_nsfw(self) -> bool:
        res = self.get_from_misc("nsfw")
        new_val = (1, 0)[int(res)]
        self.set_to_misc("nsfw", new_val)
        self.conn.commit()
        return new_val > 0

    def nhentai_block(self, nh_id, noswitch=False) -> None:
        with self.conn:
            self.cursor.execute("""select blocked from nhentai where id=?""", (nh_id,))
            res = self.cursor.fetchall()
        if len(res) > 0:
            curr_state: str = res[0][0]
            if noswitch:
                with self.conn:
                    self.cursor.execute(
                        """UPDATE nhentai SET blocked=1 WHERE id=?""", (nh_id,)
                    )
            else:
                with self.conn:
                    self.cursor.execute(
                        """UPDATE nhentai SET blocked=? WHERE id=?""",
                        (1 - int(curr_state), nh_id),
                    )
        else:
            with self.conn:
                self.cursor.execute(
                    """insert into nhentai values(?,?,?)""", (nh_id, f"fake_{nh_id}", 1)
                )
                curr_state = "1"

        if noswitch or not int(curr_state):
            logger.info("Blocked nhentai id %i", nh_id)
        else:
            logger.info("Unblocked nhentai id %i", nh_id)

    def add_meme(
        self, template_name: str, uid: int, caption: str, img_url: str
    ) -> Optional[int]:
        try:
            with self.conn:
                self.cursor.execute(
                    "INSERT INTO generated_memes(template_name, user, caption, img_url)	VALUES"
                    + " (?, ?, ?, ?)",
                    (template_name, uid, caption, img_url.strip()),
                )
            return 0
        except OperationalError as e:
            logger.warning("add_meme got fucked -> %s", str(e))

    def get_meme_templates(self) -> dict:
        with self.conn:
            self.cursor.execute(
                "SELECT template_name,template_id FROM meme_templates order by template_name asc"
            )
            res = self.cursor.fetchall()
        templates = {}
        for name, template_id in res:
            templates[name] = template_id
        return templates

    def add_meme_template(self, template_name, template_id):
        with self.conn:
            self.cursor.execute(
                """INSERT INTO meme_templates(template_name,template_id) VALUES(?,?)""",
                (template_name, template_id),
            )

    def update_polyring_feeds(
        self, feed_list: list, command_user_id: Optional[int] = None
    ):
        for blog in feed_list:
            try:
                with self.conn:
                    self.cursor.execute(
                        "INSERT INTO polyring_feeds(author,blog_url,feed_url, added_by)"
                        + " VALUES(?,?,?,?)",
                        (blog["title"], blog["url"], blog["feed"], command_user_id),
                    )
            except Exception:
                try:
                    with self.conn:
                        self.cursor.execute(
                            """UPDATE polyring_feeds SET blog_url=?, feed_url=? where author=?""",
                            (blog["url"], blog["feed"], blog["title"]),
                        )
                except OperationalError as error:
                    logger.error(str(error))
                continue

    def get_polyring_feeds(self) -> list[tuple[int, str, str]]:
        with self.conn:
            self.cursor.execute(
                """SELECT fid,feed_url,author from polyring_feeds where enabled=1"""
            )
            feeds = self.cursor.fetchall()
        return feeds

    def get_polyring_posts(self):
        with self.conn:
            self.cursor.execute(
                "SELECT pp.title, pp.description, pp.pubdate,pp.link,pf.author,pp.guid from "
                + "polyring_posts pp JOIN polyring_feeds pf on pp.fid=pf.fid where pf.enabled>0"
            )
            posts = self.cursor.fetchall()
        return posts

    def add_polyring_post(self, post, fid) -> int:
        # title, descr,pubdate,fid,link, guid
        with self.conn:
            self.cursor.execute(
                "INSERT INTO polyring_posts(title,description,pubdate,fid,link,guid)"
                + " VALUES(?,?,?,?,?,?)",
                (post.title, post.descr, post.pubdate, fid, post.link, post.guid),
            )
            self.cursor.execute("SELECT last_insert_rowid()")
            new_post_id = int(self.cursor.fetchall()[0][0])
        return new_post_id

    def get_loops(self):
        with self.conn:
            self.cursor.execute("""SELECT name,lastseen,freq FROM loops""")
            res = self.cursor.fetchall()
        return res

    def ping_loop(self, loopname: str, pingtime: float) -> None:
        with self.conn:
            self.cursor.execute(
                """UPDATE loops SET lastseen=MAX(lastseen,?) WHERE name=?""",
                (int(pingtime), loopname),
            )

    def close_down(self) -> None:
        self.conn.close()

    def add_average(self, uid: int, guess: int) -> None:
        LOWER_BOUND = 10
        UPPER_BOUND = 50_000
        if guess < LOWER_BOUND or guess > UPPER_BOUND:
            logger.info(
                "Found guess %i from uid %i to be useless, skipping.", guess, uid
            )
            return
        with self.conn:
            self.cursor.execute("""SELECT uid FROM guesses""")
        uids = [x[0] for x in self.cursor.fetchall()]
        if uid in uids:
            logger.info("updating guess")
            with self.conn:
                self.cursor.execute(
                    """UPDATE guesses SET guess=? where uid=?""", (guess, uid)
                )
        else:
            logger.info("inserting new guess")
            with self.conn:
                self.cursor.execute(
                    """INSERT INTO guesses(uid,guess) VALUES(?,?)""", (uid, guess)
                )

    def clean_guesses(self):
        with self.conn:
            self.cursor.execute("DELETE FROM guesses")

    def get_avg_guess(self, ownuid) -> int:
        with self.conn:
            self.cursor.execute(
                "SELECT avg(guess) FROM guesses WHERE uid!=?", (ownuid,)
            )  # ignore guess of the user calling the cmd
            res = self.cursor.fetchall()
        if res is None or res[0] is None or res[0][0] is None:
            return -1
        return int(res[0][0])
