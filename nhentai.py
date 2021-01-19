import requests,random,re
import skimage
import skimage.io,skimage.filters

from skimage.viewer import ImageViewer
IMPORTS=()

RANDLIMIT = 10000
SIGMADEFAULT = 20
def get_img(sigma=SIGMADEFAULT)->str:
	path = __download_random_image()

	blurpath = __blur(path,sigma)
	return blurpath
	
def __blur(path,sigma)->str:
	newname = f"{path.rstrip('jpg')}blurred.jpg"
	skimage.io.imsave(newname,skimage.filters.gaussian(skimage.io.imread(path),sigma=sigma, multichannel=True ))
	return newname


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