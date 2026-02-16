print("Importing required libraries...", "\n")
import os, shutil, re
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
from tabulate import tabulate
print("Imported required libraries.", 2 * "\n")

def table(data, headers=[]):
	print(tabulate(data, tablefmt='grid', headers=headers), "\n")

def handle_error(error = "", quit = True):
	print("\n"+ error, "\n")
	if quit:
		input()
		exit()

def sanitize_filename(title):
	"""Remove invalid characters from filename"""
	# Remove/replace characters illegal in filenames
	title = re.sub(r'[<>:"/\\|?*]', '', title)
	title = title.strip()
	# Limit length
	return title[:50] if title else "Untitled"


# directory
os.chdir(r"C:\Users\Samuel\Desktop\Remote Job\practice\python\customSeatingCards")


# load show guest list
print("Loading guest lists")
guest_list = []
try:
	with open("guests.txt", "r") as file:
		guest_list = [guest.strip() for guest in file]
except Exception as e:
	handle_error(e)

table([[guest] for guest in guest_list], headers = ["Guest List"])

def apply_text_to_template(text):
	print(f"Applying '{text}' to 'beautiful-spring-floral-frame.jpg'...")
	template = Image.open("beautiful-spring-floral-frame.jpg")
	draw = ImageDraw.Draw(template)
	lexend_deca_font = ImageFont.truetype("LexendDeca-Regular.ttf", 128)
	draw.text([i//2 for i in template.size], text, fill = "pink", font=lexend_deca_font, anchor="mm")
	return template

if os.path.exists("output"):
	shutil.rmtree("output")
os.makedirs(r"output", exist_ok=True)

for guest in guest_list:
	try:
		image = apply_text_to_template(guest)
		filename = os.path.join("output", sanitize_filename(guest) + "-invitation.jpg")
		print(f"Saving '{filename}'")
		image.save(filename)
		image.close()
	except Exception as e:
		print(e)


def close_window(count = 8):
	import time
	print()
	print(f"This window will close in {count} seconds!".upper())
	time.sleep(count)

close_window()