import os
import csv

csvpath = os.path.join('...', '/Users/nj/PythonData/python-challenge/PyBank/Resources', 'PyBank_data.csv')

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)
    totalAmount = 0

    for row in csvreader:
        totalAmount = totalAmount + int(row[1])

    totalMonths = len(list(csvreader))

print(f'Total Months: {totalMonths}')
print(f'Total: {totalAmount}')
