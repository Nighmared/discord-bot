import logging

import requests

IMPORTS = ()
logger = logging.getLogger("botlogger")


API_URL = "https://inspirobot.me/api?generate=true"


def get_img_url() -> tuple[bool, str]:
    req = requests.get(url=API_URL)
    error = req.status_code != 200
    return (error, req.content.decode())
