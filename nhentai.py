import requests,random,re
import skimage
import skimage.io,skimage.filters
import dbhandler
IMPORTS=(dbhandler)


class handler:
	SIGMADEFAULT = 20
	def __init__(self,dbhandler:dbhandler.dbhandler) -> None:
		self.db = dbhandler
		self.RANDLIMIT = int(self.db.get_from_misc("nh_random_limit"))

	def get_img(self,sigma=SIGMADEFAULT,indx_arg = None)->str:
		path,indx = self.__download_random_image(indx_arg)
		if path is None:
			blurpath = self.db.get_nhentai_path_by_id(indx)[0]
		else:
			blurpath = self._blur(path,sigma)
			self.db.add_nhentai_file(id=indx, path_to_blurred=blurpath)
		return blurpath
		
	def _blur(self,path,sigma)->str:
		newname = f"{path.rstrip('jpg')}blurred.jpg"
		skimage.io.imsave(newname,skimage.filters.gaussian(skimage.io.imread(path),sigma=(sigma,sigma), multichannel=True ))
		
		return newname


	def __download_random_image(self,indx_arg=None)->str:
		cached_ids = [x[0] for x in self.db.get_nhentai_ids()]
		blocked_ids = [x for x in self.db.get_nhentai_blocked()]
		indx = int(random.random()*self.RANDLIMIT) if indx_arg is None else indx_arg
		if indx in cached_ids and not indx in blocked_ids: #if already been downloaded
			return None,indx
		response = requests.get(f"https://nhentai.net/g/{indx}/1")
		while(response.status_code == 404 or indx in blocked_ids):
			indx = int(random.random()*self.RANDLIMIT)
			if indx in cached_ids: #if already been downloaded
				return None,indx
			response = requests.get(f"https://nhentai.net/g/{indx}/1")
		
		cont = response.text
		match = re.search('(https://i\.nhentai\.net).*?\"',cont)
		link = match.group(0).rstrip('"')
		print("[nhentai.py] freshly downloaded ",link)
		img_response = requests.get(link,stream=True)
		file = open(f"nhentai/{indx}.jpg",'wb')
		for chunk in img_response.iter_content(1024):
			file.write(chunk)
		file.close()
		
		path = f"nhentai/{indx}.jpg"
		return (path,indx)
	
	def nhentai_block(self,id)->int:
		try:
			cached_ids = [x[0] for x in self.db.get_nhentai_ids()]
			if not int(id) in cached_ids:
				return 3
			self.db.nhentai_block(id)
			return 0
		except:
			return 1
