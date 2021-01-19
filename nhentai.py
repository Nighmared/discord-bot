import requests,random,re

IMPORTS=()

RANDLIMIT = 10000

def get_img()->str:
	response = requests.get(f"https://nhentai.net/g/{int(random.random()*RANDLIMIT)}/1")
	while(response.status_code == 404): response = requests.get(f"https://nhentai.net/g/{int(random.random()*RANDLIMIT)}/1")
	cont = response.text
	match = re.search('(https://i\.nhentai\.net).*?\"',cont)
	link = match.group(0).rstrip('"')
	print("[nhentai.py] ",link)
	return link


#>>> while rep.status_code==404: rep =requests.get(f"https://nhentai.net/g/{int(random.random()*1000)}/1")
