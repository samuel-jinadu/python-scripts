print("Importing required libraries...", "\n")
import os, ocrmypdf, shutil
from pathlib import Path
print("Imported required libraries.", 2*"\n")



# set working dir
os.chdir(r"C:\Users\Samuel\Desktop\Remote Job\practice\python\ocrPdfs")

# gt pdf paths
pdfs = list(Path().glob("*.pdf"))

# make output folder
if os.path.exists("output"):
	shutil.rmtree("output")

os.makedirs(r"C:\Users\Samuel\Desktop\Remote Job\practice\python\ocrPdfs\output", exist_ok=True)


for pdf in pdfs:
	try:
		print(f"Running ocr on '{pdf}'")
		ocrmypdf.ocr(
			str(pdf), 
			os.path.join("output", str(pdf.name)), 
			rotate_pages=True, 
			redo_ocr=True, 
			tesseract_timeout=600,  # Increase from 180 to 600 seconds per page
            skip_big=False,         # Don't skip large images
            output_type='pdfa',     # PDF/A ensures text layer is embedded
            continue_on_soft_render_error=True,  # Skip corrupted pages
            jobs=1                   # Single thread to avoid Windows multiprocessing issues
            )
		print(f"'{pdf.name}' saved!")
	except Exception as e:
		print(e)
		continue

def close_window(count = 8):
	from countdown import countdown
	countdown(mins = 0, secs=count)

close_window()