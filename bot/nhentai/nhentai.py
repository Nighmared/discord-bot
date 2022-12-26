import logging
import random
import re
from typing import Optional

import requests
import skimage
import skimage.filters
import skimage.io
from bs4 import BeautifulSoup

from bot.sql import dbhandler

IMPORTS = (dbhandler,)
logger = logging.getLogger("botlogger")


with open("nhentai/tags.blacklist", "r") as f:
    NONO_TAGS = [x.strip() for x in f.readlines()]


class Handler:
    SIGMADEFAULT = 20

    def __init__(self, dbhandler_instance: dbhandler.Dbhandler) -> None:
        self.db_instance = dbhandler_instance
        try:
            self.RANDLIMIT = int(self.db_instance.get_from_misc("nh_random_limit"))
        except Exception:
            self.RANDLIMIT = 1000

    def get_img(self, sigma=SIGMADEFAULT, indx_arg=None) -> str:
        path, indx = self.__download_random_image(indx_arg)
        if path is None:
            blurpath = self.db_instance.get_nhentai_path_by_id(indx)[0]
        else:
            blurpath = self._blur(path, sigma)
            self.db_instance.add_nhentai_file(nh_id=indx, path_to_blurred=blurpath)
        return blurpath

    def _blur(self, path, sigma) -> str:
        newname = f"{path.rstrip('jpg')}blurred.jpg"
        skimage.io.imsave(
            newname,
            skimage.filters.gaussian(
                skimage.io.imread(path), sigma=(sigma, sigma), multichannel=True
            ),
        )

        return newname

    def __download_random_image(
        self, indx_arg=None
    ) -> tuple[Optional[str], Optional[int]]:
        cached_ids = [x[0] for x in self.db_instance.get_nhentai_ids()]
        blocked_ids = [int(x) for x in self.db_instance.get_nhentai_blocked()]
        if indx_arg and indx_arg in blocked_ids:
            return (
                None,
                indx_arg,
            )  # don't waste time on tag lookup if its already blocked anyway

        if indx_arg:
            resp = requests.get(f"https://nhentai.net/g/{indx_arg}/")
            if self.illegal_tags(resp, indx_arg):
                self.db_instance.nhentai_block(indx_arg)
                return None, indx_arg

        indx = int(random.random() * self.RANDLIMIT) if indx_arg is None else indx_arg
        if indx in cached_ids and indx not in blocked_ids:  # if already been downloaded
            return None, indx

        response = requests.get(f"https://nhentai.net/g/{indx}")

        while (
            response.status_code == 404
            or indx in blocked_ids
            or self.illegal_tags(response, indx)
        ):
            indx = int(random.random() * self.RANDLIMIT)
            if indx in cached_ids:  # if already been downloaded
                return None, indx
            response = requests.get(f"https://nhentai.net/g/{indx}")

        response = requests.get(f"https://nhentai.net/g/{indx}/1")

        cont = response.text
        match = re.search(r'(https://i\.nhentai\.net).*?"', cont)
        if match is None:
            return None, indx
        link = match.group(0).rstrip('"')
        logger.info(f"Freshly downloaded {link}")
        img_response = requests.get(link, stream=True)
        file = open(f"nhentai/{indx}.jpg", "wb")
        for chunk in img_response.iter_content(1024):
            file.write(chunk)
        file.close()

        path = f"nhentai/{indx}.jpg"
        return (path, indx)

    def nhentai_block(self, nh_id) -> int:
        try:
            cached_ids = [x[0] for x in self.db_instance.get_nhentai_ids()]
            if not int(nh_id) in cached_ids:
                return 3
            self.db_instance.nhentai_block(nh_id)
            return 0
        except Exception:
            return 1

    def illegal_tags(self, response: requests.Response, nh_id: int) -> bool:
        soup = BeautifulSoup(response.content, features="lxml")
        tag_links = soup.find_all("a", {"class": "tag"})
        for tag in tag_links:
            tag = tag.find("span", {"class": "name"}).text

            if tag.lower() in NONO_TAGS:
                logger.info(
                    f"Found tag violating policy, blocking id {nh_id}.  [tag={tag}]"
                )
                self.db_instance.nhentai_block(nh_id, True)
                return True
        return False
