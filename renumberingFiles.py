#imports
from pathlib import Path


# input
inputFolder = Path(input("Give the absolute path of the folder you want the files copied from: "))
if inputFolder == Path():
	inputFolder = Path(r"C:\Users\Samuel\Desktop\Remote Job\practice\python\renumberingFiles")

prefix = input("Enter the prefix of the filenames(default is 'spam'): ")
if not prefix:
	prefix = "spam"

suffix = input("Enter the suffix of the filenames(default is '.txt'): ").strip(".").lower()
if not suffix:
	suffix = "txt"

""" main code -  a program that finds all files with a given prefix, such as spam001.txt,
spam002.txt, and so on, in a single folder and locates any gaps in the num￾bering 
(such as if there is a spam001.txt and a spam003.txt but no spam002
.txt). Have the program rename all the later files to close this gap."""

print("\n", inputFolder, "\n")


# get the filenames with the ritgh prefixes

prefix_filename_paths = list(inputFolder.glob(f"{prefix}*.{suffix}"))
prefix_filename_paths.sort()

print("\n", prefix_filename_paths, "\n")

# Rename files to remove gaps
for i, filepath in enumerate(prefix_filename_paths, start=1):
	# Create new filename with sequential number
	new_name = f"{prefix}{i:03d}.{suffix}"
	new_path = inputFolder / new_name
	
	# Only rename if names are different
	if filepath.name != new_name:
		filepath.rename(new_path)
		print(f"Renamed: {filepath.name} -> {new_name}")

input()