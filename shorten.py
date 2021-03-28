import requests

BASE_URL = "https://api.shrtco.de/v2/shorten?url="

IMPORTS = ()


def shorten_link(url:str)->tuple:
	'''
		Method to shorten a given url using the shrtco.de API
		@Parameters
			url:str		url to be shortened
		@Returns
			(errorcode:int,result:str)	
						errorcode: int indicating whether operation succeeded or failed
						result: on success, new url of shortened link, else error description
	'''
	request_url = BASE_URL.join(url.strip())
	response = requests.get(url=request_url).json()
	if not response["ok"]:
		return (1,response["error"])
	else:
		return (0,response["result"]["short_link3"])
