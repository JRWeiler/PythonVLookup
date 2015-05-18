import csv
yRecords = []
tRecords = []
output = []

def buildArray(filename, array):
    rowArray = []
    with open(filename, 'r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter = ' ', quotechar = '|')
        for row in csvReader:
            rowArray = ', '.join(row).split(',')
            array.append(rowArray)

buildArray('yesterday.csv', yRecords)
buildArray('today.csv', tRecords)

for yRecord in yRecords:
    for tRecord in tRecords:
        if yRecord[0] == tRecord[0]:
            output.append(yRecord[0] + "," + yRecord[1] + "," + tRecord[1])

print output
