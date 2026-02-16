#! python 3
# pw.py

import sys, pyperclip

PASSWORDS = {
	'email': "dsdfwfcdaWdefwew324fd3c34r"
}

if len(sys.argv) < 2:
	print('Usage: py pw.py [account] - copy account password')
	sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('the password is now in your clipboard')
else:
	print("No such account exists")