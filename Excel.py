#Import Libraries
import re
import xlsxwriter

#Create a list and open the data file and prompt user to enter parameter
list = []
with open("file.txt","r") as f:
    s = input("Enter Parameter:")

#Regular expression to extract data from input parameter by user and add to list
    for line in f:
        t = (re.search(re.escape(s) + r"([.0-9]+)",line).group(1))
        list.append(t)
    print(list)

#Open a new excel workbook
workbook = xlsxwriter.Workbook('Write_Data.xlsx')
worksheet = workbook.add_worksheet()
my_list = list

#Send data from the list to row 1 in the excel file
for row_num, data in enumerate(my_list):
    worksheet.write(row_num, 1, data)
workbook.close()
