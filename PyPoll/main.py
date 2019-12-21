import os
import csv

def getUnique(inputList):
    return list(set(inputList))

def resetValue(value1):
    value1 = 0
    return (value1)

def outputFileBuilder(value1, inputDictonary):
    outputString = (
            'Election Results\n'
            '-------------------------\n'
            f'Total Votes: {value1}\n'
            '-------------------------\n'
            )
    l = {int(k):v for k,v in inputDictonary.items()}
    rl = list(l.items())
    rl.sort(reverse=True)
    winner = f'{rl[0]}'
    startPosition = winner.find(',') + 3
    endPosition = winner.find(':')
    winnerName = winner[startPosition:endPosition]
    for listValue in rl:
         outputString+=(f'{listValue[1]}\n')
    outputString+=('-------------------------\n'
                    f'Winner: {winnerName}\n'
                  '-------------------------'
                  )
    return outputString

dirname = os.path.dirname(__file__)
csvpath = os.path.join(dirname, 'PyPoll_data.csv')
outputpath = os.path.join(dirname, 'PyPoll_Output.txt')

totalVotes = 0
candidateCount = 0
maxCount = 0
resultList = {}

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)

    csvdata = list(csvreader)

    totalVotes = len(csvdata)

    candidateList = getUnique(list(zip(*csvdata))[2])

    for candidate in candidateList:
        for row in csvdata:
            if row[2] == candidate:
                candidateCount = candidateCount + 1
        candidatePercent = round((candidateCount/totalVotes)*100, 3)
        resultList[f"{candidateCount}"] =f"{candidate}: {candidatePercent}% ({candidateCount})"
        candidateCount = resetValue(candidateCount)
        candidatePercent = resetValue(candidatePercent)

output = outputFileBuilder(totalVotes, resultList)

print(output)

with open(outputpath, 'w', newline='') as outputfile:
    outputfilewriter = outputfile.write(output)
