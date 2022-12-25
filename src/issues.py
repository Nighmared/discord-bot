import logging
from typing import Optional, Union

import requests

repo_name = "discord-bot"
author = "nighmared"

logger = logging.getLogger("botlogger")

IMPORTS = ()

PASSING = "https://raw.githubusercontent.com/Nighmared/discord-bot/master/src/issues_passing.png"
FAILING = "https://raw.githubusercontent.com/Nighmared/discord-bot/master/src/issues_failing.png"


def getIssues() -> list[Union[tuple[int, int], tuple[int, str, str]]]:
    url = f"https://api.github.com/repos/{author}/{repo_name}/issues"
    r = requests.get(url)
    if r.status_code != 200:
        # 	print(f"[issues.py] (getIssues) {r.status_code} <- fucky response  from gh")
        logger.error(f"GitHub gave fucky response code ({r.status_code})")
        return [(-1, -1)]
    else:
        res = r.json()
        out = []
        for issue in res:
            tag_db_s = ""
            for tag in issue["labels"]:
                tag_db_s += f'{tag["name"]};'
            out.append(
                (issue["number"], issue["title"], tag_db_s[:-1])
            )  # dont want last ;
        out.sort()
        return out


def get_badge_link() -> str:

    url = f"https://api.github.com/repos/{author}/{repo_name}/actions/runs"
    res = requests.get(url)
    parsed = res.json()
    runs = parsed["workflow_runs"]
    indx = 0
    conclusion: Optional[str] = None
    while indx < len(runs) and (conclusion := runs[indx]["conclusion"]) is None:
        indx += 1
    if conclusion == "success":
        return PASSING
    return FAILING
