print(">>> Importing required libraries...", "\n")
import yt_dlp, pyperclip, os, re, unicodedata, sys, tldextract
from time import sleep
print(">>> Imported required libraries.", 2*"\n")

def clean_filename(title):
	if not title:
		return "tiktok_video"  # FAIL POINT: Hardcoded fallback could overwrite files
	title = re.sub(r'\s*\[\d+\]\s*', '', title)
	title = re.sub(r'#\w+\s*', '', title)
	title = re.sub(r'[\.\s]+$', '', title)
	title = re.sub(r'\s+', ' ', title).strip()
	title = unicodedata.normalize('NFKD', title)
	
	return title

def download(url):
	# FAIL POINT: yt_dlp might not extract title before download starts
	# FAIL POINT: Some TikTok URLs block yt_dlp or require cookies
	print(">>> Getting and cleaning filename")
	with yt_dlp.YoutubeDL({'quiet': True}) as ydl:
		info = ydl.extract_info(url, download=False)
		raw_title = info.get('title', '')
	
	# Clean the title for filename
	clean_title = clean_filename(raw_title)
	
	# FAIL POINT: If clean_title ends up empty after cleaning, falls back to ID
	if not clean_title:
		clean_title = info.get('id', 'tiktok_video')
	
	opts = {
		'format': "worstvideo*/worst",
		'restrict_filenames': True,
		# Use cleaned title as filename, fallback to video ID if cleaning fails
		'outtmpl': f'{clean_title}.%(ext)s',
		# FAIL POINT: If file already exists with same name, yt_dlp may skip or overwrite
		# depending on version. No 'nooverwrites' option set here.
	}
	print(f">>> Downloading {clean_title}")
	with yt_dlp.YoutubeDL(opts) as ydl:
		ydl.download([url])

def is_tiktok_url(url):
	extracted = tldextract.extract(url)
	return extracted.domain == 'tiktok' and extracted.suffix == 'com'

# FAIL POINT: Hardcoded path still crashes on other machines
os.chdir(r"C:\Users\Samuel\Desktop\Remote Job\practice\python\downloadTiktokVideo")

print(">>> The tiktok url in your clipboard will be used")
url = pyperclip.paste()
if is_tiktok_url(url):
	print(f">>> url is '{url}'")

while not is_tiktok_url(url):
	url = pyperclip.paste()
	if is_tiktok_url(url):
		print(f">>> url is '{url}'")
		break
	sleep(1)

try:
	download(url)
	print(">>> This window will close in 5s")
	sleep(5)
except Exception as e:
	print(">>>", e)
	input()