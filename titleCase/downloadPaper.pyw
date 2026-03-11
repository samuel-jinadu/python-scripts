import pyperclip, winsound, re, pyautogui, os
from PIL import Image
from pyautogui import ImageNotFoundException

def smart_title_case(text):
		text = text.title()
		"""Convert to title case while preserving certain words."""
		# Words to keep lowercase (except at start of string)
		lowercase_words = {'a', 'an', 'and', 'as', 'at', 'but', 'by', 'for', 
						  'in', 'nor', 'of', 'on', 'or', 'so', 'the', 'to', 'up', 'yet'}
		
		# Words to keep uppercase
		uppercase_words = {'api', 'url', 'http', 'https', 'www', 'id', 'pdf', 
						  'csv', 'json', 'xml', 'html', 'sql', 'ui', 'ux'}
		
		words = text.split()
		result_words = []
		
		for i, word in enumerate(words):
			# Check if entire word is uppercase (acronym)
			if word.isupper():
				result_words.append(word)
			# Check if word should remain uppercase
			elif word.lower() in uppercase_words:
				result_words.append(word.upper())
			# Check if word should remain lowercase (not first word)
			elif word.lower() in lowercase_words and i > 0:
				result_words.append(word.lower())
			# Otherwise, apply title case
			else:
				# Handle hyphenated words
				if '-' in word:
					parts = word.split('-')
					formatted_parts = []
					for j, part in enumerate(parts):
						if part.lower() in lowercase_words and j > 0:
							formatted_parts.append(part.lower())
						elif part.lower() in uppercase_words:
							formatted_parts.append(part.upper())
						else:
							formatted_parts.append(part.capitalize())
					result_words.append('-'.join(formatted_parts))
				else:
					result_words.append(word.capitalize())
		
		return ' '.join(result_words)
def sanitize_filename(title):
	"""Remove invalid characters from filename"""
	# Remove/replace characters illegal in filenames
	title = re.sub(r'[<>:"/\\|?*]', '', title)
	title = title.strip()
	return title




try:
	heliumWin = pyautogui.getWindowsWithTitle("Helium")[0]

	pyautogui.keyDown('alt')
	pyautogui.keyUp('alt')
	heliumWin.activate()

	pyautogui.hotkey('ctrl', 'c')

	text = pyperclip.paste()

	result = text.replace("\n"," ").replace("\r", "").replace(": ", " - ").replace('"', "").replace("'", "").strip()
	result = result.replace("'", "'").replace("'", "'").replace("'", "'")
	result = sanitize_filename(result)
	result = smart_title_case(result)
	
	pyperclip.copy(result)

	pyautogui.keyDown('alt')
	pyautogui.keyUp('alt')
	heliumWin.activate()
	
	os.chdir(r"C:\Users\Samuel\Desktop\Remote Job\practice\python\titleCase")
	imageDownloadButton = Image.open('download-button.png').convert('RGB')
	boxDownloadButton = pyautogui.locateOnScreen(imageDownloadButton, confidence=0.8)
	centerDownloadButton = pyautogui.center(boxDownloadButton)
	pyautogui.click(centerDownloadButton)
	
	pyautogui.sleep(2)

	
	try:
		imageAddressBar = Image.open('address-bar.png').convert('RGB')
		boxAddressBar = pyautogui.locateOnScreen(imageAddressBar, confidence=0.8)
	except ImageNotFoundException:
		imageClickSpace = Image.open("address-bar-click-space.png").convert("RGB")
		boxClickSpace = pyautogui.locateOnScreen(imageClickSpace, confidence=0.8)
		centerClickSpace = pyautogui.center(boxClickSpace)
		pyautogui.click(centerClickSpace)
		pyautogui.sleep(0.1)
		pyperclip.copy(r"C:\Users\Samuel\Desktop\Books\Research\papers")
		pyautogui.sleep(0.1)
		pyautogui.hotkey('ctrl', 'v')
		pyautogui.sleep(0.1)
		pyautogui.press("Enter")
		pyautogui.sleep(0.1)
		for i in range(6):
			pyautogui.press("tab")
			pyautogui.sleep(0.1)
		

	pyperclip.copy(result)

	pyautogui.sleep(0.1)
	pyautogui.hotkey('ctrl', 'v')
	winsound.MessageBeep()
	pyautogui.sleep(0.1)
	pyautogui.press("Enter")
	
except:
	winsound.MessageBeep(winsound.MB_ICONHAND)