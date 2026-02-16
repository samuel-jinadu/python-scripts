print("Importing required libraries...", "\n")
import os
from pathlib import Path
print("Imported required libraries.", 2*"\n")

print("This program identifies all photo folders in your system", "\n")

threshold = input("Enter a threshold for identifying photofolder in percentage of photos in a folder (default is 80%): ").strip()
if not threshold.isdigit():
	print("Threshold set to default '80'")
	threshold = 80
else:
	threshold = int(threshold)

print()

for root, dirs, files in os.walk(r'C:\Users\Samuel'):
	if len(files) == 0:
		continue
	patterns = ["*.png", "*.jpeg", "*.webp", "*.gif", "*.jpg"]
	img_filepaths = [p for pattern in patterns for p in Path(root).glob(pattern)]
	percentage = (len(img_filepaths)/len(files)) *100

	if percentage >= threshold:
		print(f"'{root}' is a photofolder!")

print()
input("Press any key to quit")
input("Are you sure?")