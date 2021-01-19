import requests,random,re
import skimage
import skimage.io,skimage.filters
import dbhandler

from skimage.viewer import ImageViewer
IMPORTS=(dbhandler)


class handler:
	SIGMADEFAULT = 20
	def __init__(self,dbhandler:dbhandler.dbhandler) -> None:
		self.db = dbhandler
		self.RANDLIMIT = int(self.db.get_from_misc("nh_random_limit"))

	def get_img(self,sigma=SIGMADEFAULT)->str:
		path,indx = self.__download_random_image()
		if path is None:
			blurpath = self.db.get_nhentai_path_by_id(indx)[0]
		else:
			blurpath = self.__blur(path,sigma)
			self.db.add_nhentai_file(id=indx, path_to_blurred=blurpath)
		return blurpath
		
	def __blur(self,path,sigma)->str:
		newname = f"{path.rstrip('jpg')}blurred.jpg"
		skimage.io.imsave(newname,skimage.filters.gaussian(skimage.io.imread(path),sigma=sigma, multichannel=True ))
		return newname


	def __download_random_image(self)->str:
		cached_ids = [x[0] for x in self.db.get_nhentai_ids()]
		indx = int(random.random()*self.RANDLIMIT)
		if indx in cached_ids: #if already been downloaded
			return None,indx
		response = requests.get(f"https://nhentai.net/g/{indx}/1")
		while(response.status_code == 404):
			indx = int(random.random()*self.RANDLIMIT)
			if indx in cached_ids: #if already been downloaded
				return None,indx
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
		return (path,indx)