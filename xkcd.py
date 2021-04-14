import requests

IMPORTS = ()

CURR_URL = "https://xkcd.com/info.0.json"

def get_comic(id:int)->dict:
	req = requests.get(url=_make_url(id))
	if req.status_code == 404:
		return {
			"success":False,
			"error": "No comic found for this number",
		}
	elif req.status_code == 200:
		j = req.json()
		return {
			"success":True,
			"num":j["num"],
			"title":j["safe_title"],
			"img_url":j["img"],
		}

def get_latest()->dict:
	req = requests.get(url = CURR_URL)
	if req.status_code != 200:
		return {
			"success":False,
			"error":f".. something went wrong af... \n status code: {req.status_code}"
		}
	else:
		j = req.json()
		return {
			"success":True,
			"num":j["num"],
			"title":j["safe_title"],
			"img_url":j["img"],
		}


def _make_url(id:int)->str:
	return f"https://xkcd.com/{id}/info.0.json"
