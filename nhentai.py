import requests,random,re
import skimage
import skimage.io,skimage.filters
from skimage.viewer import ImageViewer
IMPORTS=()

RANDLIMIT = 10000

def get_img()->str:
	path = __download_random_image()

	__blur(path)
	return path
	
def __blur(path)->None:
	SIGMA = 25
	skimage.io.imsave(path,skimage.filters.gaussian(skimage.io.imread(path),sigma=(SIGMA,SIGMA), multichannel=True ))



def __download_random_image()->str:
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
	file = open(f"nhentai/{indx}.jpg",'wb')
	#file.write(response.raw)
	for chunk in img_response.iter_content(1024):
		file.write(chunk)
	file.close()
	
	path = f"nhentai/{indx}.jpg"
	return path