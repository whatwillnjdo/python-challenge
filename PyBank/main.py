import os
import csv

dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname, 'PyBank_data.csv')
outputpath = os.path.join(dirname, 'PyBank_Output.txt')

totalAmount = 0
currentAmountChange = 0
nextAmount = 0
previousAmountChange = 0
greatestMonth = ''
lowestAmountChange = 0
lowestMonth = ''
output = ''

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)

    csvdata = list(csvreader)

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

output = (
        'Financial Analysis\n'
        '----------------------------\n'
        f'Total Months: {totalMonths}\n'
        f'Total: ${totalAmount}\n'
        f'Average  Change: ${averageChange}\n'
        f'Greatest Increase in Profits: {greatestMonth} (${previousAmountChange})\n'
        f'Greatest Decrease in Profits: {lowestMonth} (${int(lowestAmountChange)})\n'
        )

print(output)

with open(outputpath, 'w', newline='') as outputfile:
    outputfilewriter = outputfile.write(output)
