import csv
yRecords = []
tRecords = []
output = []

#Function to build an array from values in a csv file
def buildArray(filename, array):
    rowArray = []
    with open(filename, 'r') as csvInput:
        csvReader = csv.reader(csvInput, delimiter = ' ', quotechar = '|')
        for row in csvReader:
            rowArray = ', '.join(row).split(',')
            array.append(rowArray)

#Call the buildArray function to populate yRecords and tRecords
buildArray('yesterday.csv', yRecords)
buildArray('today.csv', tRecords)

#Create output file and for every record in yRecords, see if there is a match in tRecords
#If found, write the 'ID' (yRecord[0] in this case, but could also use tRecord[0])
#and the associated values from each file in a single row delimited by a comma
with open('output.csv', 'wb') as csvOutput:
    csvWriter = csv.writer(csvOutput, delimiter = ' ', quotechar = '|', quoting = csv.QUOTE_MINIMAL)
    for yRecord in yRecords:
        for tRecord in tRecords:
            if yRecord[0] == tRecord[0]:
                csvWriter.writerow([yRecord[0]+','+yRecord[1]+','+tRecord[1]])


