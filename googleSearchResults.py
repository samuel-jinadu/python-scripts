#! python3
# googleSearchResults.py - Opens several Google search results

import requests, sys, webbrowser, bs4

print("Googling...")
res = requests.get(f"https://www.google.com/search?q={"+".join(sys.argv[1:])}")
res.raise_for_status()

links = bs4.BeautifulSoup(res.text).select("a.zReHs")

# abandoned because google is strict af these days