print("Importing required libraries...", "\n")
import os, shutil
from PIL import Image
from pathlib import Path
from tabulate import tabulate
print("Imported required libraries.", 2*"\n")

LOGO_FILENAME = 'logo.png'

def handle_error(error = ""):
	print("\n"+ error)
	input()
	exit()

def table(data, headers=[]):
	print(tabulate(data, tablefmt='grid', headers=headers), "\n")



# change working directory
os.chdir(r"C:\Users\Samuel\Desktop\Remote Job\practice\python\addALogo")

# announce instructions
print("This program adds a logo, 'logo.png' to all images in the 'input' folder")

# Choose corner to put logo
corners_raw = ["top-left", "top-right", "bottom-left", "bottom-right"]
corners = [(index + 1, item) for index, item in enumerate(corners_raw)]
table(corners)

selected_corner = input("Select a corner (enter number or text): ").strip().lower()

# Check if it's a number
if selected_corner.isdigit() and 1 <= int(selected_corner) <= 4:
	selected_corner = corners_raw[int(selected_corner) - 1]
else:
	# Try to match by substring
	matches = [c for c in corners_raw if selected_corner in c]
	
	if len(matches) == 0:
		print(f"'{selected_corner}' not recognized. Using default: top-left")
		selected_corner = corners_raw[0]
	elif len(matches) == 1:
		selected_corner = matches[0]
	else:
		print(f"Multiple matches for '{selected_corner}': {matches}")
		print("Using first match...")
		selected_corner = matches[0]

print(f"Logo will be placed at: {selected_corner}")


# check if logo.png exists
if not os.path.exists("logo.png"):
	handle_error("'logo.png' is missing!" )

# check if input files exist
input_folder = r"input"
input_filepaths = list(Path(input_folder).glob("*.png")) + list(Path(input_folder).glob("*.jpeg")) + list(Path(input_folder).glob("*.webp")) + list(Path(input_folder).glob("*.gif"))
if not input_filepaths:
	handle_error("There's no files in input")

# load images
try:
	print("Loading images...", "\n")
	logo = Image.open(LOGO_FILENAME)
	input_images = [Image.open(filepath) for filepath in input_filepaths]
	print("Images loaded", "\n")
except Exception as e:
	handle_error(e)

def add_logo(image, position = (10,10), logo = logo):
	image.paste(logo, position, logo)
	return image


# add logo
processed_images = []
for image in input_images:
	try:
		print(f"Adding logo to {Path(image.filename).name}")
		position = (10,10)
		size = image.size
		if selected_corner == "top-left":
			processed_images.append(add_logo(image))
		elif selected_corner == "top-right":
			processed_images.append(add_logo(image, position = (size[0] - logo.size[0], 0)))
		elif selected_corner == "bottom-left":
			processed_images.append(add_logo(image, position = (0, size[1] - logo.size[1])))
		elif selected_corner == "bottom-right":
			processed_images.append(add_logo(image, position = (size[0] - logo.size[0], size[1] - logo.size[1])))
	except ValueError:
		handle_error(f"'{LOGO_FILENAME}' is too large or '{Path(image.filename).name}' is too small")
	except Exception as e:
		handle_error(e)
	


# Delete previous output folder if it exists
if os.path.exists('output'):
	shutil.rmtree('output')

# save files
os.makedirs(r"C:\Users\Samuel\Desktop\Remote Job\practice\python\addALogo\output", exist_ok=True)
for image in processed_images:
	filename = Path(image.filename).name
	print(f"Saving {filename}")
	image.save(os.path.join('output', filename))
	print(f"Saved {filename}!", "\n")


def close_window(count = 8):
	import time
	print(f"This window will close in {count} seconds!")
	time.sleep(count)

close_window()