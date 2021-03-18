import requests

IMPORTS = ()

with open(".imgflip_creds.txt","r") as cred_file:
	IMGFLIP_ACC, IMGFLIP_PW = cred_file.read().strip().split(";")

TEMPLATE_IDS = {
	"spongebob_mocking":102156234,
	"evil_kermit":84341851,
}

def get_meme(template_name:str, caption:str)->tuple: #returns (errorcode:int, img_url:str, error_descr:str)
	if template_name not in TEMPLATE_IDS.keys():
		return (3,None,"Invalid template name")
	
	template_id = TEMPLATE_IDS[template_name]
	p_req = requests.post(
		url= "https://api.imgflip.com/caption_image",
		data = {
			"template_id":f"{template_id}",
			"username":IMGFLIP_ACC,
			"password":IMGFLIP_PW,
			"text0":caption
		}
	)
	if p_req.status_code !=200:
		return (1,None, f"Request didn't work, response code is {p_req.status_code}")
	
	try:
		return (0,p_req.json()["data"]["url"], None)
	except KeyError:
		return (1, "", p_req.content.decode())

