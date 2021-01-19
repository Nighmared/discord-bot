import requests,random,re

IMPORTS=()

RANDLIMIT = 10000

def get_img()->str:
	indx = int(random.random()*RANDLIMIT)
	response = requests.get(f"https://nhentai.net/g/{indx}/1")
	while(response.status_code == 404):
		indx = int(random.random()*RANDLIMIT)
		response = requests.get(f"https://nhentai.net/g/{indx}/1")
	
	cont = response.text
	match = re.search('(https://i\.nhentai\.net).*?\"',cont)
	link = match.group(0).rstrip('"')
	print("[nhentai.py] ",link)
	img_response = requests.get(link,stream=True)
	file = open("nhentai/SPOILER_{indx}.jpg",'wb')
	#file.write(response.raw)
	for chunk in img_response.iter_content(1024):
		file.write(chunk)
	file.close()
	
	path = f"nhentai/SPOILER_{indx}.jpg"
	
	return link


#>>> while rep.status_code==404: rep =requests.get(f"https://nhentai.net/g/{int(random.random()*1000)}/1")
