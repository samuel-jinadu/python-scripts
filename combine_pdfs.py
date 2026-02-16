print("Importing required libraries...", "\n")
import pypdf, os
from pathlib import Path
print("Imported required libraries.", 2*"\n")

os.chdir(r"C:\Users\Samuel\Desktop\Remote Job\practice\python\combine_pdfs")

pdf_paths = list(Path(".").glob("*.pdf"))

if len(pdf_paths) == 0:
	print(r"No pdfs found in 'C:\Users\Samuel\Desktop\Remote Job\practice\python\combine_pdfs'!")
	input()
	exit()

writer = pypdf.PdfWriter()

print("Merging files...", "\n")
for pdf in pdf_paths:
	try:
		print(f"Appending {pdf}")
		writer.append(pdf)
	except Exception as e:
		print(f"Faild to append {pdf}", "\n")

print("Saving merged pdf...")
with open("merged.pdf", "wb") as file:
	writer.write(file)

print("Done!")
input()