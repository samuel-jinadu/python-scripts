#! python3
# downloadXkcd.py - downloads a random set of 100 xkcd comics

try:
	import requests, os
	from bs4 import BeautifulSoup
	from pathlib import Path
	
	destinationFolder = Path(r"C:\Users\Samuel\Desktop\Remote Job\practice\python\downloadXkcd")
	url = "https://c.xkcd.com/random/comic/"
	input()
	
	for i in range(1, 11):
		print(f"Downloading random page", "using", url, "...")
		input("Enter to cotinue")
		res = requests.get(url)
		res.raise_for_status()
		html = BeautifulSoup(res.text, "html.parser")
		comicUrl = html.find('meta', property="og:image").get("content")
		comicTitle = html.find(id='ctitle').get_text()
		print(f"Downloading comic '{comicTitle}'...")
		imgRes = requests.get(comicUrl)
		with open(destinationFolder / Path(comicTitle).with_suffix(Path(comicUrl).suffix), "wb") as imageFile:
			for chunk in imgRes.iter_content(100000):
				imageFile.write(chunk)
		input("Enter to cotinue")
	print("Done")
	input()

except Exception as e:
	print(e)
	input()