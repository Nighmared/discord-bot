import logging
from datetime import datetime

IMPORTS = ()
logger = logging.getLogger("botlogger")


class Uptime:
    def __init__(self, starttime: datetime):
        self.start = starttime

    def get_uptime(self):
        curr = datetime.now()
        diff = curr - self.start
        secs = diff.seconds
        mins = int(secs / 60)
        hours = int(mins / 60)
        days = diff.days
        years = int(days / 365)
        secs %= 60
        mins %= 60
        hours %= 24
        days %= 365
        weeks = int(days / 7)
        days %= 7
        out = ""

        if years > 0:
            out += f"{years} Year" + (" ", "s ")[years > 1]
        if weeks > 0:
            out += f"{weeks} Week" + (" ", "s ")[weeks > 1]

        if days > 0 and years < 1:
            out += f"{days} Day" + (" ", "s ")[days > 1]
        if hours > 0 and years < 1:
            out += f"{hours} Hour" + (" ", "s ")[hours > 1]
        if mins > 0 and weeks < 1:
            out += f"{mins} Minute" + (" ", "s ")[mins > 1]
        if days < 1 and secs > 0:
            out += f"{secs} Second" + ("", "s")[secs > 1]
        return out.strip()

    def get_now_utc(
        self,
    ):  # dumb wrapper function so i dont have to import datetime separately in commandhandler
        return datetime.utcnow()


def get_now_utc():
    return datetime.utcnow()
