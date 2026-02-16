import openpyxl, pprint, os

#
os.chdir(r"C:\Users\Samuel\Desktop\Remote Job\practice\python\Automate_the_Boring_Stuff_3e_onlinematerials")

#
print("Opening census data excel file...", "\n")
sheet = openpyxl.load_workbook("censuspopdata.xlsx")["Population by Census Tract"]
print("Census data loaded...", "\n")

#
county_data = {}

print("Constructing data struture...", "\n")
for row in range(2, sheet.max_row +1):
	state = sheet["B" + str(row)].value
	county = sheet["C" + str(row)].value
	pop = sheet["D" + str(row)].value

	county_data.setdefault(state, {})
	county_data[state].setdefault(county, {"tracts": 0, "pop": 0})

	county_data[state][county]["tracts"] +=1
	county_data[state][county]["pop"] += int(pop)
	print(f"row {row} 'State: {state} - County: {county}' added to data structure...")

print(2*"\n")
print("Finished constructing data structure...", "\n")

print("Writing in python file...", "\n")
with open("census2010_practice.py", "w") as file:
	file.write("allData = " + pprint.pformat(county_data))
print("Finished...")


input()