import os
import csv
from collections import Counter

csv_no=['1','2']

for tocheck in csv_no :
    pybank_csv = os.path.join('raw_data', 'election_data_' + tocheck+'.csv')
    with open(pybank_csv, 'r', encoding="utf-8") as csvFile:
        voteid=[]
        country=[]
        candidate=[]
        candidate_list=[]
        csvReader = csv.reader(csvFile, delimiter=',')

        # Skipp headers
        next(csvReader, None)
        
        for row in csvReader:

            # Append data from the row
            voteid.append(row[0])
            country.append(row[1])
            candidate.append(row[2])
            no_of_votes=len(voteid)
            #candidate.sort()
            #print(candidate)

    myset1=[]
    myset2=[]
    myset=set(candidate)
    myset1.append(Counter(candidate).keys()) # equals to list(set(words))
    myset2.append(Counter(candidate).values()) # counts the elements' frequency
    print("Election Results")
    print("---------------------")
    print("Total Votes : "+str(no_of_votes))
    print("---------------------")
    s = set([1, 2, 3])
    for i in myset:
     print(""+str(list(myset1)[str(i)]))