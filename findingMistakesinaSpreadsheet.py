print("Importing required libraries...", "\n")
import ezsheets, sys
print("Libraries imported", "\n")

try:
	print("Getting spreadsheet...", "\n")
	ss = ezsheets.Spreadsheet("https://docs.google.com/spreadsheets/d/1jDZEdvSIh4TmZxccyy0ZXrH-ELlrwq8_YYiZrEOB4jg/edit?usp=sharing")
except Exception as e:
	print(e)
	input()
	sys.exit()

sheet = ss.sheets[0]
rows = sheet.getRows()[1:]  # Remove the first row (headers)

try:
	for row in rows:
		if not ((int(row[0]) * int(row[1])) == int(row[2])):
			print("There is a mistake on row:", rows.index(row) + 2)
except Exception as e:
	print(e)


input()