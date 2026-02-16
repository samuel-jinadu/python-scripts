import pyautogui
from random import randint, uniform

while True:
	pyautogui.move(randint(-5,5), randint(-5,5))
	pyautogui.countdown(uniform(1,100))