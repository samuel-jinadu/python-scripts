from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import randint


browser = webdriver.Firefox()
browser.get("https://play2048.co/")
html = browser.find_element(By.TAG_NAME, "html")

keyList = [Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT]

while True:
	html.send_keys(keyList[randint(0,3)])