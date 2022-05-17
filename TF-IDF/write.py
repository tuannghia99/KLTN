
# import xlsxwriter module
import xlsxwriter

count = 0

workbook = xlsxwriter.Workbook('Example.xlsx')
worksheet = workbook.add_worksheet()
 
# Start from the first cell.
# Rows and columns are zero indexed.
row = 0
column = 0
 
import io

f1 = io.open("cut1.vi", "r", encoding="utf-8")
 
# iterating through content list
for item in f1:
    item = item.strip()
    # write operation perform
    worksheet.write(row, column, item)
 
    # incrementing the value of row by one
    # with each iterations.
    row += 1
     
workbook.close()