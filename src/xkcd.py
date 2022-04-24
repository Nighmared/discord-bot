import logging

import requests

IMPORTS = ()
logger = logging.getLogger("botlogger")


CURR_URL = "https://xkcd.com/info.0.json"


def get_comic(comic_id: int) -> dict:
    req = requests.get(url=_make_url(comic_id))
    if req.status_code == 404:
        return {
            "success": False,
            "error": "No comic found for this number",
        }
    elif req.status_code == 200:
        j = req.json()
        return {
            "success": True,
            "num": j["num"],
            "title": j["safe_title"],
            "img_url": j["img"],
            "alt": j["alt"],
        }


def get_latest() -> dict:
    req = requests.get(url=CURR_URL)
    if req.status_code != 200:
        return {
            "success": False,
            "error": f".. something went wrong af... \n status code: {req.status_code}",
        }
    j = req.json()
    return {
        "success": True,
        "num": j["num"],
        "title": j["safe_title"],
        "img_url": j["img"],
        "alt": j["alt"],
    }


def _make_url(comic_id: int) -> str:
    return f"https://xkcd.com/{comic_id}/info.0.json"


def