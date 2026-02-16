import pyperclip
text = pyperclip.paste()

# split into lines and add bulletpoint
splitText = text.split("\n")
for index, line in enumerate(splitText):
	splitText[index] = "- " + splitText[index] + "\n"

# join modified lines
text = ""
for line in splitText:
	text += line


pyperclip.copy(text)
print("Results".center(12, '='))
print()
print(text)
print()
print("copied to clipboard!")
input()