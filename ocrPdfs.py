import os
import shutil
import subprocess
import sys
from pathlib import Path

# Auto-install dependencies
try:
	import fitz  # pymupdf
except ImportError:
	subprocess.check_call([sys.executable, "-m", "pip", "install", "pymupdf", "pikepdf"])
	import fitz

print("Processing PDFs...\n")

os.chdir(r"C:\Users\Samuel\Desktop\Remote Job\practice\python\ocrPdfs")
pdfs = list(Path().glob("*.pdf"))

if os.path.exists("output"):
	shutil.rmtree("output")
os.makedirs("output", exist_ok=True)

def get_text(pdf_path):
	"""Extract text using PyMuPDF"""
	try:
		doc = fitz.open(str(pdf_path))
		text = ""
		for page in doc:
			text += page.get_text()
		doc.close()
		return text.strip()
	except:
		return ""

for pdf in pdfs:
	output_path = os.path.join("output", pdf.name)
	
	try:
		print(f"Processing '{pdf.name}'...")
		existing_text = get_text(pdf)
		
		# CASE 1: No text found - Use PyMuPDF's built-in OCR
		if len(existing_text) < 10:
			print("  → No text found, OCR with PyMuPDF...")
			
			doc = fitz.open(str(pdf))
			ocr_doc = fitz.open()  # New output document
			
			for page_num, page in enumerate(doc):
				print(f"    Page {page_num + 1}...")
				
				# Render page to image at 300 DPI
				mat = fitz.Matrix(300/72, 300/72)
				pix = page.get_pixmap(matrix=mat)
				
				# OCR using pdfocr_tobytes - creates PDF with text layer
				try:
					ocr_pdf_bytes = pix.pdfocr_tobytes(language="eng")
					ocr_page_doc = fitz.open("pdf", ocr_pdf_bytes)
					ocr_doc.insert_pdf(ocr_page_doc)
					ocr_page_doc.close()
				except Exception as ocr_err:
					print(f"      ⚠ OCR failed for page {page_num + 1}: {ocr_err}")
					# Insert original page as fallback
					ocr_doc.insert_pdf(doc, from_page=page_num, to_page=page_num)
				
				pix = None  # Free memory
			
			# Save final OCR'd PDF - NO linear=True (deprecated)
			ocr_doc.save(output_path, garbage=4, deflate=True)
			ocr_doc.close()
			doc.close()
			
		# CASE 2: Has text - Just optimize
		else:
			print("  → Has text, optimizing...")
			doc = fitz.open(str(pdf))
			doc.save(output_path, garbage=4, deflate=True)
			doc.close()
		
		# Verify text is selectable
		final_text = get_text(output_path)
		if len(final_text) < 10:
			print(f"  ⚠ Warning: Still no selectable text!")
		else:
			orig_size = os.path.getsize(pdf) / 1024
			new_size = os.path.getsize(output_path) / 1024
			ratio = new_size / orig_size if orig_size > 0 else 0
			print(f"  ✓ Done: {orig_size:.0f}KB → {new_size:.0f}KB ({ratio:.1f}x), {len(final_text)} chars")
			
	except Exception as e:
		print(f"  ✗ Failed: {e}")
		import traceback
		traceback.print_exc()
		# Fallback: copy original
		shutil.copy(str(pdf), output_path)

print("\nAll done. Check the 'output' folder.\n")

def close_window(count=8):
	from countdown import countdown
	countdown(mins=0, secs=count)

close_window()