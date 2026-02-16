print("Importing required libraries...", "\n")
import ezsheets, sys, os, shutil
from pathlib import Path


os.chdir(r"C:\Users\Samuel\Desktop\Remote Job\practice\python")

print(rf"Current input-output directory is {os.getcwd()}\convertSpreadsheetToOtherFormats" + "\n")


# get first excel file in folder
target_folder = r'.\convertSpreadsheetToOtherFormats'

while not list(Path(target_folder).glob("*.xlsx")):
	print("\n"+"No Excel files found in directory!", "\n")
	input("Press enter to try again:")
else:
	try:
		filepath = list(Path(target_folder).glob("*.xlsx"))[0]
		print("\n", f"Uploading: {filepath}", "\n")
		ss = ezsheets.upload(str(filepath))
		print(f"Uploaded sheet: {ss.title}", "\n")
	except Exception as e:
		print(e)
		input()
	try:
		downloaded_file = ss.title + '.csv'
		print(f"Downloading {downloaded_file}...", "\n")
		actual_filename = ss.downloadAsCSV()
		destination_path = os.path.join(target_folder, downloaded_file)
		shutil.move(actual_filename, destination_path)
		print(f'File downloaded and moved to: {destination_path}', "\n")
	

		downloaded_file = ss.title + '.pdf'
		print(f"Downloading {downloaded_file}...", "\n")
		actual_filename = ss.downloadAsPDF()
		destination_path = os.path.join(target_folder, downloaded_file)
		shutil.move(actual_filename, destination_path)
		print(f'File downloaded and moved to: {destination_path}', "\n")
	except Exception as e:
		print(e)
		input()
	
input()