print("Importing required libraries...", "\n")
import ezsheets, sys

if len(sys.argv) != 4:
	print("Usage: python addBoringcoinTransaction.py [sender] [recipient] [amount]")
	sys.exit()



try:
	print("Getting super secure blockchain...", "\n")
	ss = ezsheets.Spreadsheet("https://docs.google.com/spreadsheets/d/1DT2E7-hpvRFIhvKDbAAgMPqJ1tqCjbgG4GGAyoVprFs/edit?usp=sharing")
except Exception as e:
	print(e)
	sys.exit()


sheet = ss.sheets[0]

accounts = {}

for row in sheet.getRows():
	sender, recipient, amount = row[0], row[1], int(row[2])

	if sender == "PRE-MINE":
		accounts.setdefault(recipient, 0)
		accounts[recipient] += amount
	else:
		accounts.setdefault(sender, 0)
		accounts.setdefault(recipient, 0)
		accounts[sender] -= amount
		accounts[recipient] += amount


sender, recipient, amount = sys.argv[1:]

if sender not in accounts.keys():
	print(f"'{sender}' cannot send because the account doesn't exist in the blockchain")
	sys.exit()
elif int(amount) > accounts[sender]:
	print(f"'{sender}' cannot send '{amount}'")
	print(f"'{accounts[sender]}' will be sent instead")
	amount = accounts[sender]

# update blockchain

print(f"Performing transaction with sender: {sender}; recipient: {recipient}; amount: {amount}...", "\n")
sheet.updateRow(sheet.rowCount + 1, [sender, recipient, amount])

print("Transaction complete")