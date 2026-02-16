#imports
import os, send2trash
from pathlib import Path


# input
inputFolder = Path(input("Give the absolute path of the folder you want the files copied from: "))

if not inputFolder.is_dir():
	inputFolder = Path(r"C:\Users\Samuel\Desktop\Remote Job\practice\python\deletingUnneededFiles")

# main code

print("This program will delete all files in the target folder larger than 100MB (but it does't delete anythng because i dont believe in giving a program i made that much power yet on my pc)", 2 * "\n")


for folderName, subfolders, filenames in os.walk(inputFolder):
	for filename in filenames:
		filepath = Path(folderName) / filename
		folder_path_str = os.path.abspath(Path(folderName))
		filesize = round(os.path.getsize(filepath) / (1024 * 1024), 2)
		filesize_str = str(filesize)  + " MB"
		if filesize > 100:
			print("Do you reeally want to delete", "\n" + filename, "\n" + "located in", f"'{folder_path_str}'", "\n" + "with size of:", filesize_str)
			confirmation = input("Y/N (anything other than Y/y is a no): ").upper()
			if confirmation == "Y":
				print("I will now delete", f"'{filename}'")
			else:
				print("I will not delete", f"'{filename}'")
			print(2 * "\n")

input()

# -----------Interesting Concept below-------------


"""
#imports
import os, send2trash
from pathlib import Path


# input
inputFolder = Path(input("Give the absolute path of the folder you want the files copied from: "))

if not inputFolder.is_dir():
	inputFolder = Path(r"C:\Users\Samuel\Desktop\Remote Job\practice\python\deletingUnneededFiles")

# main code

print("This program will delete all files in the target folder larger than 100MB (but it does't delete anythng because i dont believe in giving a program i made that much power yet on my pc)", 2 * "\n")

# CRITICAL BUG FIX: First collect all files to delete, THEN ask for confirmation
# This prevents issues with os.walk() when files are deleted during iteration
files_to_consider = []

# First pass: collect all large files without modifying anything
for folderName, subfolders, filenames in os.walk(inputFolder):
	for filename in filenames:
		filepath = Path(folderName) / filename
		folder_path_str = os.path.abspath(Path(folderName))
		filesize = round(os.path.getsize(filepath) / (1024 * 1024), 2)
		filesize_str = str(filesize)  + " MB"
		if filesize > 100:
			files_to_consider.append((filepath, filename, folder_path_str, filesize_str))

# Second pass: ask about deletion (still won't actually delete per your comment)
for filepath, filename, folder_path_str, filesize_str in files_to_consider:
	print("Do you reeally want to delete", "\n" + filename, "\n" + "located in", f"'{folder_path_str}'", "\n" + "with size of:", filesize_str)
	confirmation = input("Y/N (anything other than Y/y is a no): ").upper()
	if confirmation == "Y":
		print("I will now delete", f"'{filename}'")
		# If you ever enable actual deletion, use:
		# send2trash.send2trash(filepath)  # Safer than permanent delete
	else:
		print("I will not delete", f"'{filename}'")
	print(2 * "\n")

input()
"""