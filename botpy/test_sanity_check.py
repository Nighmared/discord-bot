import logging
from datetime import datetime
from random import random
from time import sleep

from botpy.handler import handler

XKCD_NUM_LIMIT = 2000

RH_STRINGLEN_LIMIT = 30


class Test_Basics:
    def test_imports_tuples(self):
        """
        makes sure all modules that are reloaded on a softreload actually have
        the correct structure, specifically that they all have an "IMPORTS" **tuple**
        """
        import botpy.handler.handler as msgh  # same as above

        print("sdf\n")
        print("\033[0;32m")
        for impo in msgh.IMPORTS:
            if (
                type(impo.IMPORTS) != tuple
            ):  # make sure that all modules have an IMPORTS tuple defined,
                # otherwise softreload can break
                print("\033[0;31m", end="")
                print(f"Failed Module: {impo.__name__}")
                print("\033[0m")
                assert False  # fail
            else:
                print(f"Valid Module: {impo.__name__}".ljust(40), end="\n")
            for subimp in impo.IMPORTS:
                if (
                    type(subimp.IMPORTS) != tuple
                ):  # same but for imports of the imported modules
                    print("\033[0;31m", end="")
                    print(f"Failed Module: {subimp.__name__}".ljust(40))
                    print("\033[0m", end="")
                    assert False  # fail it here
                else:
                    print(f"Valid Module: {subimp.__name__}".ljust(40))

        print("\033[0m")
        print("\n\n")

    def test_logger_everywhere(self):
        """
        Checks that all modules have a logger defined, basically just making it
        ready for further improvements
        """
        import botpy.handler.handler as msgh

        for impo in msgh.IMPORTS:
            print("checking " + impo.__name__)
            assert type(impo.logger) == logging.Logger

            for subi in impo.IMPORTS:
                print("checking " + subi.__name__)
                assert type(subi.logger) == logging.Logger

    def test_import_all(self):
        """
        Hopefully this would fail if there was some obvious and hard syntax error somewhere
        """
        import discord

        from botpy import bot
        from botpy.cmd import commandhandler
        from botpy.inspirobot import inspirobot
        from botpy.issues import issues
        from botpy.loops import polyring
        from botpy.meme import meme
        from botpy.msglist import msglist
        from botpy.neko import neko
        from botpy.nhentai import nhentai
        from botpy.robohash import robohash
        from botpy.shorten import shorten
        from botpy.sql import dbhandler
        from botpy.stalk import stalk
        from botpy.uptime import uptime
        from botpy.xkcd import xkcd

        anti_lint = (  # noqa: F841
            discord,
            bot,
            commandhandler,
            dbhandler,
            handler,
            inspirobot,
            issues,
            meme,
            msglist,
            neko,
            robohash,
            polyring,
            shorten,
            stalk,
            uptime,
            xkcd,
            nhentai,
        )


class Test_APIs:
    def test_xkcd(
        self,
    ):  # run example xkcd call to make sure json structure is still okay
        import botpy.xkcd.xkcd as xkcd

        res = xkcd.get_latest()
        assert res["success"]
        res = xkcd.get_comic(int(random() * XKCD_NUM_LIMIT))
        assert res["success"]

    def test_robohash(self):  # -...
        import botpy.robohash.robohash as robohash

        dummy_string_len = int(random() * RH_STRINGLEN_LIMIT + 10)
        dummy_string = ""
        for i in range(dummy_string_len):
            dummy_string += chr(97 + int(random() * 26))

        robohash.get_embed(dummy_string)  # check that it doesnt fail

    def test_issues(self):
        import botpy.issues.issues as issues

        res = issues.getIssues()
        assert res != (-1, -1)

    def test_inspiro(self):
        import botpy.inspirobot.inspirobot as inspirobot

        res = inspirobot.get_img_url()
        assert not res[0]  # first element is boolean error flag

    def test_uptime(self):
        import botpy.uptime.uptime as uptime

        a_time = datetime.now()
        tracker = uptime.Uptime(a_time)
        sleep(1)
        res_string = tracker.get_uptime()
        print(res_string)
        assert "Second" in res_string
        assert not ("Seconds" in res_string)
        assert not ("Year" in res_string)
        assert not ("Day" in res_string)
        assert not ("Hour" in res_string)
        assert not ("Minute" in res_string)
        sleep(3)
        res_string = tracker.get_uptime()
        assert "Seconds" in res_string
        assert not ("Second " in res_string)
        assert not ("Year" in res_string)
        assert not ("Day" in res_string)
        assert not ("Hour" in res_string)
        assert not ("Minute" in res_string)


class Test_Invalid_Input:
    def test_robohash(self):
        import botpy.robohash.robohash as robohash

        robohash.get_embed("")

    def test_xkcd(self):
        import botpy.xkcd.xkcd as xkcd

        res = xkcd.get_comic(-1)
        assert not res["success"]


class Tests_Slow_Cases:
    def test_shorten(self):  # same as for xkcd
        import botpy.shorten.shorten as shorten

        res = shorten.shorten_link("ethz.wtf")
        assert res[0] == 0  # no error

    def test_shorten_invalid(self):
        import botpy.shorten.shorten as shorten

        res = shorten.shorten_link("")
        assert res[0] != 0
