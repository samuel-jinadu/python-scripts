import re, os

os.chdir(r'C:\Users\Samuel\Desktop\Remote Job\practice\python\madLIbs')

print(os.getcwd(), "\n")

noun = input("Enter a noun: ")
adjective = input("\nEnter an adjective: ")
verb = input("\nEnter a verb: ")

text = "The ADJECTIVE panda walked to the NOUN and to VERB it. A nearby NOUN was unaffected by these events."

with open(r'C:\Users\Samuel\Desktop\Remote Job\practice\python\madLIbs\input.txt', "r") as file:
	print("\ninput: ", text)
	print()
	file_content = file.read()
	if file_content == "":
		text = file.read()
	text = re.sub(r'NOUN', noun, text)
	text = re.sub(r'ADJECTIVE', adjective, text)
	text = re.sub(r'VERB', verb, text)
	print("\noutput: "text)

with open(r'C:\Users\Samuel\Desktop\Remote Job\practice\python\madLIbs\output.txt', "w") as file:
	file.write(text)

input()