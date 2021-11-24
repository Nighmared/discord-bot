import logging

import requests

BASE_URL = "https://api.shrtco.de/v2/shorten?url="

IMPORTS = ()
logger = logging.getLogger("botlogger")


def shorten_link(url: str) -> tuple:
    """
    Method to shorten a given url using the shrtco.de API
    @Parameters
            url:str		url to be shortened
    @Returns
            (errorcode:int,result:str)
                                    errorcode: int indicating whether operation succeeded or failed
                                    result: on success, new url of shortened link, else error description
    """
    try:
        request_url = BASE_URL + url.strip()
    except AttributeError:
        return (1, "Invalid input, doesnt have strip() method")
    response = requests.get(url=request_url).json()
    if not response["ok"]:
        return (1, response["error"])
    else:
        return (0, "http://" + response["result"]["short_link3"])
