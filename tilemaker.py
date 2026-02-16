print("Importing required libraries...", "\n")
import os
from PIL import Image
from pathlib import Path
print("Imported required libraries.", 2*"\n")


def handle_error(error = "", quit = True):
	print("\n"+ error, "\n")
	if quit:
		input()
		exit()

def close_window(count = 8):
	import time
	print(f"This window will close in {count} seconds!")
	time.sleep(count)


def has_transparency(img):
	"""Check if image has alpha channel or transparency info."""
	# Check for alpha channel modes (RGBA, LA, PA)
	if img.mode in ('RGBA', 'LA', 'PA'):
		return True
	# Check for palette-based images with transparency
	if img.mode == 'P' and 'transparency' in img.info:
		return True
	return False

# Usage example:
# image = Image.open("image.png")
# if has_transparency(image):
#     print("Image has transparency")
# else:
#     print("Image has no transparency")


# announcements
print("The program will tile all images in the folder")

# change working directory
os.chdir(r"C:\Users\Samuel\Desktop\Remote Job\practice\python\tilemaker")

# get images to tile
patterns = ["*.png", "*.jpeg", "*.webp", "*.gif", "*.jpg"]
input_filepaths = [p for pattern in patterns for p in Path().glob(pattern)]

if not input_filepaths:
	handle_error("There are no valid images in th folder!")

# get the number of tiles both horizontal and vertial
horizontal = ""
vertical = ""

while not horizontal.isdigit() or not vertical.isdigit():
	try:
		inputs = input("Enter the number of tiles (horizontal, vertical): ").replace(" ", "")
		if "," in inputs:
			horizontal, vertical = inputs.split(",")[:2]
		else:
			horizontal, vertical = (inputs, "1")
	except Exception as e:
		handle_error(e)
	if not horizontal.isdigit() or not vertical.isdigit():
		print("They must be integers!", "\n")
else:
	horizontal = int(horizontal)
	vertical = int(vertical)

if horizontal < 1:
	horizontal = 1
if vertical <1:
	vertical = 1

def save_image(image, filename):
	filepath = Path(filename)
	if has_transparency(image):
		filepath = filepath.with_suffix('.png')
	filename = filepath.stem +"-tiled" + filepath.suffix
	if os.path.exists(filename):
		image.close()
		print(f"{filename} already exists!")
		return
	print(f"Saving '{filename}'...")
	image.save(filename)
	print(f"{filename} saved!")
	image.close()

def tile_image(image, dimensions = (1,1)):
	horizontal = dimensions[0]
	vertical = dimensions[1]

	# Pre-check to avoid MemoryError
	max_pixels = getattr(Image, 'MAX_IMAGE_PIXELS', 89478485) or 89478485
	total_pixels = image.size[0] * horizontal * image.size[1] * vertical
	
	if total_pixels > max_pixels:
		print(f"Error: Tiled image ({total_pixels} pixels) exceeds safety limit ({max_pixels})")
		if horizontal > 1 or vertical > 1:
			max_tiles = max_pixels // (image.size[0] * image.size[1])
			max_dim = int(max_tiles ** 0.5)
			new_h = min(horizontal, max(1, max_dim))
			new_v = min(vertical, max(1, max_dim))
			if new_h < horizontal or new_v < vertical:
				print(f"Retrying with reduced dimensions: {new_h}×{new_v}")
				return tile_image(image, (new_h, new_v))
		return None

	try:
		if has_transparency(image):
			if image.mode != 'RGBA':
				image = image.convert('RGBA')
			base = Image.new("RGBA", (image.size[0] * horizontal, image.size[1] * vertical), (0,0,0,0))
			for horizontal_index in range(horizontal):
				for vertical_index in range(vertical):
					position = (horizontal_index * image.size[0], vertical_index * image.size[1])
					base.paste(image, position, image)
			return base
		else:
			base = Image.new("RGB", (image.size[0] * horizontal, image.size[1] * vertical))
			for horizontal_index in range(horizontal):
				for vertical_index in range(vertical):
					position = (horizontal_index * image.size[0], vertical_index * image.size[1])
					base.paste(image, position)
			return base
	except MemoryError:
		print("Error: Out of memory when creating tiled image")
		return None

# run the tile finction on each image
print("Tiling images...")
for filepath in input_filepaths:
	image = None      # ADD THIS LINE
	tiled_image = None  # ADD THIS LINE
	try:
		image = Image.open(filepath)
		print(f"Tiling '{image.filename}'")
		tiled_image = tile_image(image, dimensions = (horizontal, vertical))
		if tiled_image == None:
			print(f"'{image.filename}' was not tiled because it would be too large!")
			image.close()
			continue
		print(f"'{image.filename}' is tiled!")
		save_image(tiled_image, image.filename)
		image.close()
	except Exception as e:
		handle_error(e, quit = False)
	finally:
		# CRITICAL FIX: Always close resources, even if an exception occurred
		if image is not None:
			image.close()
		if tiled_image is not None:
			# If save_image failed or was skipped, clean up the tiled image
			tiled_image.close()

close_window(20)