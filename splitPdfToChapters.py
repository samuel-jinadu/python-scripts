print("Importing required libraries...", "\n")
import os, fitz, re
from pathlib import Path
from tabulate import tabulate
print("Imported required libraries.", 2*"\n")

os.chdir(r"C:\Users\Samuel\Desktop\Remote Job\practice\python\splitPdfToChapters")

def print_toc(data):
	data = [(level, title[:50] + ("..." if len(title) > 50 else ""), page) for level, title, page in data]
	print(tabulate(data, headers=["Level", "Title", "Page"], tablefmt='grid'), "\n")

def handle_error(error = ""):
	print(error)
	input()
	exit()

def sanitize_filename(title):
	"""Remove invalid characters from filename"""
	# Remove/replace characters illegal in filenames
	title = re.sub(r'[<>:"/\\|?*]', '', title)
	title = title.strip()
	# Limit length
	return title[:50] if title else "Untitled"






pdf_paths = list(Path().glob("*.pdf"))
pdf_path = ""
if pdf_paths:
	pdf_path = pdf_paths[0]
else:
	handle_error("Pdf not found!")

try:
	doc = fitz.open(str(pdf_path))
	book_title = doc.name.split(".pdf")[0]
	toc = doc.get_toc()
	if not toc:
		handle_error("This pdf has no bookmarks!")
	print_toc(toc)
	try:
		level = int(input("What level do you want to do the splitting at: "))
	except ValueError:
		level = 1
	print(f"Level set to '{level}'", "\n")

	# remove any entry that is not at the selected level 
	chapters = [bookmark for bookmark in toc if bookmark[0] == level]

	if not chapters:
		handle_error("No chapters found at level " + str(level))
	else:
		print_toc(chapters)
	total_pages = len(doc)

	output_folder = r".\chapters"
	os.makedirs(output_folder, exist_ok=True)
	
	for i, (level, title, page_num) in enumerate(chapters):
		# TOC page numbers are 1-based, fitz uses 0-based
		start_page = page_num - 1
		
		# Calculate end page (next chapter start - 1, or end of document)
		if i + 1 < len(chapters):
			end_page = chapters[i + 1][2] - 2  # Next chapter start - 1
		else:
			end_page = total_pages - 1
		
		# Ensure valid range
		if start_page < 0:
			start_page = 0
		if end_page >= total_pages:
			end_page = total_pages - 1
		if start_page > end_page:
			continue
		
		# Create new PDF for this chapter
		new_doc = fitz.open()
		new_doc.insert_pdf(doc, from_page=start_page, to_page=end_page)
		
		# Set metadata and TOC
		new_doc.metadata = {
			"title": title
		}
		
		# Save
		safe_title = sanitize_filename(title)
		filename = f"{pdf_path.stem}-{safe_title}.pdf"
		filepath = os.path.join(output_folder, filename)
		
		new_doc.save(filepath)
		new_doc.close()
		
		print(f"Saved: {filename} (pages {start_page+1}-{end_page+1})")
	doc.close()
	handle_error()
	
except Exception as e:
	handle_error(e)

