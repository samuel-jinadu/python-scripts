print("Importing required libraries...", "\n")
import os, csv
from pathlib import Path
print("Imported required libraries.", 2*"\n")

os.chdir(r"C:\Users\Samuel\Desktop\Remote Job\practice\python\removeCsvHeader")
os.makedirs("headersRemoved", exist_ok=True)

csv_paths = list(Path(".").glob("*.csv"))

for filepath in csv_paths:
	print(f"Removing headers from {filepath}...")

	with open(filepath, "r", encoding="utf-8") as file:
		content = list(csv.reader(file))
		if content == [] or len(content) < 2:
			print(f"{filepath} is empty")
			continue
		content = content[1:]
		with open(os.path.join("headersRemoved", str(filepath)), "w", newline="", encoding="utf-8") as output:
			print(f"Saving '{filepath}'")
			writer = csv.writer(output)
			for row in content:
				writer.writerow(row)
			print(f"Saved '{filepath}'!", 2*"\n")

input()