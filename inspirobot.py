import requests

API_URL = "https://inspirobot.me/api?generate=true"

def get_img_url()->tuple:
	req = requests.get(url=API_URL)
	error = req.status_code != 200
	return (error, req.content.decode())
