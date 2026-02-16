print("Importing required libraries...", "\n")
import os, pandas
from pathlib import Path
print("Imported required libraries.", 2*"\n")

os.chdir(r"C:\Users\Samuel\Desktop\Remote Job\practice\python\excelcsvConverter")
os.makedirs("csvOutput", exist_ok=True)


filepaths = list(Path(".").glob("*.xlsx"))

if len(filepaths) == 0:
	print("No excel files found!")
	input()
	exit()

for filepath in filepaths:
	try:
		print(f"Opening {str(filepath)}...")
		excel_dict = pandas.read_excel(str(filepath), sheet_name = None)
	except Exception as e:
		print(e, "\n")
		continue

	for sheet, data in excel_dict.items():
		safe_name = sheet.replace(" ", "_").replace("/", "_")
		csv_filename = os.path.join("csvOutput", f"{filepath.stem}_{safe_name}.csv")
		try:
			print(f"Converting '{filepath}' to '{csv_filename}'...")
			data.to_csv(csv_filename, index = False, encoding = "utf-8")
			print(f"'{csv_filename}' saved!", "\n")
		except Exception as e:
			print(e)

input()
		