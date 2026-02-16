import sys, openpyxl, os
from pathlib import Path
print()

row = 1
no = 1

if len(sys.argv) == 3:
	row = int(sys.argv[1])
	no = int(sys.argv[2])
else:
	print("The syntax is 'python blankRowInserter.py [row] [number of rows to insert]'", "\n")
	sys.exit(1)

os.chdir(r"C:\Users\Samuel\Desktop\Remote Job\practice\python\blankRowInserter")

print(f"Current working directory is {os.getcwd()}", "\n")


filenames = list(Path().glob("*.xlsx"))


for filename in filenames:
	print(f"Opening {filename}...", "\n")
	wb = openpyxl.load_workbook(filename)
	sheet = wb.active

	print(f"Adding {no} row(s) to {filename} at row {row}...", "\n")
	sheet.insert_rows(row, no)

	print(f"Saving {filename}...", "\n")
	wb.save(filename)

	print(f"Saved {filename}", "\n")