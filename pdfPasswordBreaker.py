print("Importing required libraries...", "\n")
import pypdf, os
from pathlib import Path
print("Imported required libraries.", 2*"\n")

print(r"This program will perform a simple dictionary attack on all encrypted pdfs in the folder")
os.chdir(r"C:\Users\Samuel\Desktop\Remote Job\practice\python\pdfPasswordBreaker")

filenames = list(Path(".").glob("*.pdf"))

if len(filenames) == 0:
	print("No '.pdfs' were found!")
	input()
	exit()

try:
	passwords = []
	with open("dictionary.txt", "r") as dictionary:
		passwords = [line.strip() for line in dictionary]
except FileNotFoundError:
	print("Dictionary not found!")
	input()
	exit()
	


for filename in filenames:
	file_size_mb = os.path.getsize(filename) / (1024 * 1024)
	if file_size_mb > 100:
		print(f"WARNING: {filename} is {file_size_mb:.0f}MB - may cause memory issues")
		input()
		continue
	try:
		print(f"Loading {filename}...", "\n")
		reader = pypdf.PdfReader(filename)
		print(f"{filename} loaded", 2*"\n")
	except Exception as e:
		print(e)
		input()
		continue


	

	if not reader.is_encrypted:
		print(f"{filename} is not encrypted")
		continue

	print("Attempting dictionary attack...")
	decrypted = False
	for i, password in enumerate(passwords):
		# print(f"trying {password}")
		status = reader.decrypt(password)
		if status > 0:
			print("\n" + f"'{filename}' decrypted successfully with '{password}'")
			print("Saving decrypted pdf...")
			writer = pypdf.PdfWriter()
			try:
				writer.append(reader)
			except Exception as e:
				raise e
			writer.write(f'{filename.stem}-decrypted.pdf')
			print("Saved")
			decrypted = True
			break
		if i % 5000 == 0 and i > 0:
			print(f"Tried {i} passwords. Last attempt started with '{password[0].upper()}'")

	if not decrypted:
		print(f"Dictionary attack failed on {filename}!")

input()