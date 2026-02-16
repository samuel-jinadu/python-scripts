# imports
import os, re, shutil
from pathlib import Path

# inputs
inputFolder = input("Give the absolute path of the folder you want the files copied from: ")
fileExtension = input("Give the file extension of the files you want copied (default is .py): ").strip(".")
outputFolder = input("Give the absolute path of the destination folder: ")


# defaults
if inputFolder == "":
	inputFolder = Path(r"C:\Users\Samuel\Desktop\Remote Job\practice\python")
else:
	inputFolder = Path(inputFolder)

if fileExtension == "":
	fileExtension = "py"

if outputFolder	== "":
	outputFolder = Path(r"C:\Users\Samuel\Desktop\Remote Job\practice\python\selectiveCopy")
else:
	outputFolder = Path(outputFolder)



outputFolder.mkdir(parents=True, exist_ok=True)



# walk through folder
for folderName, subfolders, filenames in os.walk(inputFolder):
	for filename in filenames:
		if not filename.endswith(f".{fileExtension}"):
			continue
		try:
			# The file will be copied into the directory using its original filename
			shutil.copy2(Path(folderName) / filename, outputFolder)
			print(f"File '{filename}' copied to '{outputFolder}'")
		except FileNotFoundError:
			print("Source file or destination directory not found.")
		except PermissionError:
			print("Permission denied.")
		except Exception as e:
			print(f"An error occurred: {e}")