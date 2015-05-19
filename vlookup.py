import csv
yRecords = []
tRecords = []
output = []

def buildArray(filename, array):
    rowArray = []
    with open(filename, 'r') as csvInput:
        csvReader = csv.reader(csvInput, delimiter = ' ', quotechar = '|')
        for row in csvReader:
            rowArray = ', '.join(row).split(',')
            array.append(rowArray)

buildArray('yesterday.csv', yRecords)
buildArray('today.csv', tRecords)

with open('output.csv', 'wb') as csvOutput:
    csvWriter = csv.writer(csvOutput, delimiter = ' ', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
    for yRecord in yRecords:
        for tRecord in tRecords:
            if yRecord[0] == tRecord[0]:
                csvWriter.writerow([yRecord[0]+','+yRecord[1]+','+tRecord[1]])


