import requests
import dbhandler

IMPORTS = ()

with open(".imgflip_creds.txt","r") as cred_file:
	IMGFLIP_ACC, IMGFLIP_PW = cred_file.read().strip().split(";")


def get_meme(template_name:str, text0:str,text1:str,dbhandler:dbhandler.dbhandler)->tuple: #returns (errorcode:int, img_url:str, error_descr:str)
	TEMPLATE_IDS = dbhandler.get_meme_templates()
	if template_name not in TEMPLATE_IDS.keys():
		return (3,None,"Invalid template name",None)

	template_id = TEMPLATE_IDS[template_name]
	p_req = requests.post(
		url= "https://api.imgflip.com/caption_image",
		data = {
			"template_id":f"{template_id}",
			"username":IMGFLIP_ACC,
			"password":IMGFLIP_PW,
			"font":"arial",
			"max_font_size":"100px",
			"text0":text0,
			"text1":text1,
		}
	)
	if p_req.status_code !=200:
		return (1,None, f"Request didn't work, response code is {p_req.status_code}", None)
	
	try:
		return (0,p_req.json()["data"]["url"], None, p_req.json()["data"]["page_url"])
	except KeyError:
		return (1, "", p_req.content.decode(),None)

