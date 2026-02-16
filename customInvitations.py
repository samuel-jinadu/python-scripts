print("Importing required libraries...", "\n")
from docx import Document
import os
print("Imported required libraries.", 2*"\n")


os.chdir(r"C:\Users\Samuel\Desktop\Remote Job\practice\python\customInvitations")

print("Loading template...")



print("Loading guest list...", "\n")
with open("guests.txt", "r") as guests:
	replaced = False
	for line in guests:
		guest = line.strip()

		if not guest:
			continue
		
		print("Making invitaions based on the template...", "\n")
		doc = Document("template.docx")
		
		

		for paragraph in doc.paragraphs:
			if "[insert]" in paragraph.text:
				full_text = "".join(run.text for run in paragraph.runs)
				
				# Replace placeholder
				new_text = full_text.replace("[insert]", guest)
				
				# Clear all runs first
				for run in paragraph.runs:
					run.text = ""
				
				# Put new text in the first run (preserves its formatting)
				if paragraph.runs:
					paragraph.runs[0].text = new_text
				
				replaced = True
			# for run in paragraph.runs:
			# 	if "[insert]" in run.text:
			# 		run.text = run.text.replace("[insert]", guest)
			# 		replaced = True
		
		guest = "".join(c for c in guest if c.isalnum() or c in (' ', '-', '_')).strip()
		filename = f"{guest}-invitation.docx"
		print(f"{filename} has been created...")
		doc.save(filename)
	if not replaced:
			print("'[insert]' not found!")


print()
print("Done!")
input()