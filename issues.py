import requests
repo_name = "discord-bot"
author = "nighmared"

def getIssues()->list:
	url = f"https://api.github.com/repos/{author}/{repo_name}/issues"
	r = requests.get(url)
	if(r.status_code != 200):
		print(r.status_code,"fck")
		return [(-1,-1)]
	else:
		res = r.json()
		out = []
		for issue in res:
			out.append((issue["number"],issue["title"]))
		out.sort()
		return out
