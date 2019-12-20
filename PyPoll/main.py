import os
import csv

def getUnique(inputList):
    return list(set(inputList))

dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname, 'PyPoll_data.csv')
outputpath = os.path.join(dirname, 'PyPoll_Output.txt')

totalVotes = 0
candidateCount = 0
maxCount = 0
winnerName = ''

output = (
        'Election Results\n'
        '-------------------------\n'
        )

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)

    csvdata = list(csvreader)

    totalVotes = len(csvdata)
    output+=(
             f'Total Votes: {totalVotes}\n'
             '-------------------------\n'
             )

    candidateList = getUnique(list(zip(*csvdata))[2])

    for candidate in candidateList:
        for row in csvdata:
            if row[2] == candidate:
                candidateCount = candidateCount + 1
        candidatePercent = round((candidateCount/totalVotes)*100, 3)
        output+=f"{candidate}: {candidatePercent}% ({candidateCount})\n"
        if maxCount < candidateCount:
            maxCount = candidateCount
            winnerName = candidate
        candidateCount = 0
        candidatePercent = 0

output+=('-------------------------\n'
         f'Winner: {winnerName}\n'
         '-------------------------'
         )

print(output)

with open(outputpath, 'w', newline='') as outputfile:
    outputfilewriter = outputfile.write(output)
