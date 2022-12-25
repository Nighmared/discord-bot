import logging
from typing import Literal, Union

import requests

import dbhandler

IMPORTS = ()

logger = logging.getLogger("botlogger")

try:
    with open(".imgflip_creds.txt", "r") as cred_file:
        IMGFLIP_ACC, IMGFLIP_PW = cred_file.read().strip().split(";")
except FileNotFoundError:
    print("[MEME.PY] - no credentials found")
    logger.fatal("cant generate memes, no credentials found")


def get_meme(
    template_name: str, text0: str, text1: str, dbhandler: dbhandler.Dbhandler
) -> Union[
    tuple[Literal[0], str, None, str],
    tuple[int, None, str, None],
]:  # returns (errorcode:int, img_url:str, error_descr:str,meme_url:str)
    TEMPLATE_IDS = dbhandler.get_meme_templates()
    if template_name not in TEMPLATE_IDS.keys():
        return (3, None, "Invalid template name", None)

    template_id = TEMPLATE_IDS[template_name]
    p_req = requests.post(
        url="https://api.imgflip.com/caption_image",
        data={
            "template_id": template_id,
            "username": IMGFLIP_ACC,
            "password": IMGFLIP_PW,
            "font": "arial",
            "text0": text0,
            "text1": text1,
        },
    )
    if p_req.status_code != 200:
        return (
            1,
            None,
            f"Request didn't work, response code is {p_req.status_code}",
            None,
        )

    try:
        return (0, p_req.json()["data"]["url"], None, p_req.json()["data"]["page_url"])
    except KeyError:
        return (1, None, p_req.content.decode(), None)


def get_popular_memes() -> list:
    get = requests.get(url="https://api.imgflip.com/get_memes")
    memes = get.json()["data"]["memes"]
    res = []
    for meme in memes:
        res.append((meme["name"], meme["id"]))
    return res
