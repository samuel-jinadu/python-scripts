from pathlib import Path
import os, re

os.chdir(r'C:\Users\Samuel\Desktop\Remote Job\practice\python')

python_file_paths = list(Path(".").glob("*.py"))

results =[]

# print(python_file_paths)
pattern = r'\b' + re.escape(input("What do you want to search for: ")) + r'\b' 
print()

for filepath in python_file_paths:
    with open(filepath, "r") as file:
        text = file.readlines()
        for line in text:
            if re.search(pattern, line):
                results.append(line)
                print("\nFound pattern!", "\n", line.strip())


input()