print("Importing required libraries...", "\n")
import ezsheets, pprint

print("ezsheets and pprint imported", "\n")


try:
	print("Getting super secure blockchain...", "\n")
	ss = ezsheets.Spreadsheet("https://docs.google.com/spreadsheets/d/1DT2E7-hpvRFIhvKDbAAgMPqJ1tqCjbgG4GGAyoVprFs/edit?usp=sharing")
except Exception as e:
	print(e)
	input()


print("Super secure blockchain acquired...", "\n")
accounts = {}

for row in ss.sheets[0].getRows():
	sender, recipient, amount = row[0], row[1], int(row[2])

	if sender == "PRE-MINE":
		accounts.setdefault(recipient, 0)
		accounts[recipient] += amount
	else:
		accounts.setdefault(sender, 0)
		accounts.setdefault(recipient, 0)
		accounts[sender] -= amount
		accounts[recipient] += amount

pprint.pprint(accounts)
print()

total = 0

for amount in accounts.values():
	total += amount

print("Total Boringcoins: ", total)

input()