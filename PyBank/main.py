import os
import csv

csvpath = os.path.join('...', '/Users/nj/PythonData/python-challenge/PyBank/Resources', 'PyBank_data.csv')

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)

    csvdata = list(csvreader)

    totalAmount = 0
    currentAmountChange = 0
    nextAmount = 0
    previousAmountChange = 0
    greatestMonth = ''
    lowestAmountChange = 0
    lowestMonth = ''

    for row in csvdata:
        totalAmount = totalAmount + int(row[1])
        currentAmountChange = int(row[1]) - nextAmount
        nextAmount = int(row[1])
        currentMonth = row[0]

        if previousAmountChange < currentAmountChange:
            previousAmountChange = currentAmountChange
            greatestMonth = currentMonth

        if lowestAmountChange > currentAmountChange:
            lowestAmountChange = currentAmountChange
            lowestMonth = currentMonth

    totalMonths = len(csvdata)
    averageChange = round(totalAmount/totalMonths, 2)

print(f'Total Months: {totalMonths}')
print(f'Total: ${totalAmount}')
print(f'Average  Change: ${averageChange}')
print(f'Greatest Increase in Profits: {greatestMonth} (${previousAmountChange})')
print(f'Greatest Decrease in Profits: {lowestMonth} (${int(lowestAmountChange)})')
