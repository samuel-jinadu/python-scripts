import pyperclip, winsound, webbrowser, pyautogui, os

# Simple logging setup at the top:
import logging

os.chdir(r"C:\Users\Samuel\Desktop\Remote Job\practice\python\summariseInSimpleTerms")
logging.basicConfig(
    filename='summariseInSimpleTerms_error_log.txt',
    level=logging.ERROR,
    format='%(asctime)s - %(message)s'
)

try:
	heliumWin = pyautogui.getWindowsWithTitle([t for t in pyautogui.getAllTitles() if "Helium" in t][0])[0]

	pyautogui.keyDown('alt')
	pyautogui.keyUp('alt')
	heliumWin.activate()

	center_x = heliumWin.left + (heliumWin.width // 2)
	center_y = heliumWin.top + (heliumWin.height // 2)
	pyautogui.click(center_x, center_y)
	pyautogui.hotkey('ctrl', 'a')
	pyautogui.sleep(0.2)
	pyautogui.hotkey('ctrl', 'c')
	pyautogui.sleep(0.2)  # Wait for clipboard



	text = pyperclip.paste()
	
	result = text + (2 * "\n") + "summarise in simple terms (translate to english)"
	
	pyperclip.copy(result)
	pyautogui.sleep(0.2) 
	 
	
	url = "https://chat.deepseek.com/new"  # Many AI chats support /new for fresh conversations
	
	# Open browser (always opens new tab/window)
	webbrowser.open(url)
	
	# Wait for browser to open and page to load
	pyautogui.sleep(5)  # Adjust based on your connection speed
	
	# Simulate Ctrl+V to paste wherever the cursor is
	pyautogui.hotkey('ctrl', 'v')
	pyautogui.press("Enter")
	winsound.MessageBeep()
	
	pyautogui.sleep(0.2)
	
	format_text = ("task: format your most recent output as a markdown and give it a brief title\n\n"
					"make sure to: add title of papers as sources at the end in italics\n\n"
					"don't use: tables\n\n"
					"be careful not to make hanging explanation formats like this:\n"
					"```\n"
					"🏆 External/Material Success (Most Important):\n"
					"    Money, expensive property, prestigious job...\n"
					"```")
	pyperclip.copy(format_text)
	
	
except Exception as e:
	winsound.MessageBeep(winsound.MB_ICONHAND)
	logger = logging.getLogger(__name__)
	logger.error(f"An error occurred: {str(e)}")


