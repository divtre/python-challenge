import os
import csv

csv_no=['1','2']

for tocheck in csv_no :
    pybank_csv = os.path.join('raw_data', 'election_data_' + tocheck+'.csv')
    with open(pybank_csv, 'r', encoding="utf-8") as csvFile:
        voteid=[]
        country=[]
        candidate=[]
        csvReader = csv.reader(csvFile, delimiter=',')

        # Skipp headers
        next(csvReader, None)
        
        for row in csvReader:

            # Append data from the row
            voteid.append(row[0])
            country.append(row[1])
            candidate.append(row[1])

            no_of_months=len(voteid)
        print("no of vote"+str(no_of_months))