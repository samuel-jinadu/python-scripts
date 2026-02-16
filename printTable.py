tableData = [
    ['apples', 'oranges', 'cherries', 'banana'],    # Column 0
    ['Alice', 'Bob', 'Carol', 'David'],             # Column 1  
    ['dogs', 'cats', 'moose', 'goose']              # Column 2
]

# def transformListToString(toBeTransformed):
#     m = ""
#     for index, item in enumerate(toBeTransformed):
#         if index != len(toBeTransformed) - 1:
#             m += str(item)
#             m += " "
#         else:
#             m += " "
#             m += str(item)
#             break
#     return m


def printTable(tableData):
    # Step 1: Calculate the maximum width for each column
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        for item in tableData[i]:
            if len(item) > colWidths[i]:
                colWidths[i] = len(item)
    
    # Step 2: Print the table row by row
    for row_index in range(len(tableData[0])):  # For each row
        row_string = ""
        for col_index in range(len(tableData)):  # For each column
            # Add the item right-justified using the column's max width
            row_string += tableData[col_index][row_index].rjust(colWidths[col_index]) + " "
        print(row_string)


printTable(tableData)
input()