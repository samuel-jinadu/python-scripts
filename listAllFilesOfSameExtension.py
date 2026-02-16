import os, pyperclip, pyautogui
from pathlib import Path
from tabulate import tabulate

print("This program lists all files of the same extension or certain keywords")


VIDEO_EXTENSIONS = ["*.mp4", "*.avi", "*.mov", "*.wmv", "*.flv", "*.mkv", "*.webm", "*.m4v", "*.mpg", "*.mpeg", "*.3gp", "*.ts", "*.mts", "*.m2ts"]

IMAGE_EXTENSIONS = ["*.png", "*.jpeg", "*.webp", "*.gif", "*.jpg"]

isFolder = False

def table(data):
	data = [[str(path)[:100] + ("..." if len(str(path)) > 100 else "")] for path in data]
	if not isFolder:
		print(tabulate(data, headers=["Filenames"], tablefmt='grid'), "\n")
	else:
		print(tabulate(data, headers=["Folders"], tablefmt='grid'), "\n")

def handle_error(error = ""):
	print(error)
	input()


while True:
	try:
		path = pyperclip.paste()
		if path == "Videos":
			path = r"C:\Users\Samuel\Videos"
		elif path == "Downloads":
			path = r"C:\Users\Samuel\Downloads"
		if not os.path.isdir(path):
			print(">>> You need to have copied a valid folder")
			print(">>> Try again in 7s")
			pyautogui.countdown(7)
			continue
		print(f">>> Current working directory has been set to '{path}'")
		os.chdir(path)
	
		extensions = input(">>> Enter the extensions (xxx or keyword): ").lower().strip()
	
		files = None
		isFolder = False
		if "image" in extensions or "img" in extensions:
			files = [p.name for pattern in IMAGE_EXTENSIONS for p in Path().glob(pattern)]
		elif "vid" in extensions:
			files = [p.name for pattern in VIDEO_EXTENSIONS for p in Path().glob(pattern)]
		elif extensions == "folder" or extensions == "folders":
			files = [item for item in os.listdir(path) if os.path.isdir(item)]
			isFolder = True
		elif len(extensions.split(",")) > 1 and extensions.split(",")[-1] != "":
			extensions = [ ("*."+ extension) for extension in extensions.split(",")]
			files = [p.name for pattern in extensions for p in Path().glob(pattern)]
		else:
			files = list(Path().glob("*."+ extensions))

		table(files)
		copyBool = input("Do you want to copy this list to clipboard (y/n)").lower().strip()
		if "y" in copyBool:
			pyperclip.copy(str([file for file in files]))
	except Exception as e:
		handle_error(e)
		continue


