import os
import csv

dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname, 'PyPoll_data.csv')
outputpath = os.path.join(dirname, 'PyPoll_Output.txt')

totalVotes = 0
candidate1Count = 0
candidate2Count = 0
candidate3Count = 0
candidate4Count = 0

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)

    csvdata = list(csvreader)

    for row in csvdata:
        if row[2].upper() == 'KHAN':
            candidate1Count = candidate1Count + 1

totalVotes = len(csvdata)
candidate1Percent = round((candidate1Count/totalVotes)*100, 3)

output = (
        'Election Results\n'
        '-------------------------\n'
        f'Total Votes: {totalVotes}\n'
        f'Khan: {candidate1Percent}% ({candidate1Count})\n'
)

print(output)

with open(outputpath, 'w', newline='') as outputfile:
    outputfilewriter = outputfile.write(output)
