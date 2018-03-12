import os
import csv
import datetime
import re
import us

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

csv_no=['1','2']

for tocheck in csv_no :
    pybank_csv = os.path.join('raw_data', 'employee_data' + tocheck+'.csv')
    with open(pybank_csv, 'r', encoding="utf-8") as csvFile:
        EmpID=[]
        FName=[]
        LName=[]
        DOB=[]
        SSN=[]
        State=[]
        csvReader = csv.reader(csvFile, delimiter=',')

        # Skipp headers
        next(csvReader, None)
        
        for row in csvReader:
            EmpID.append(row[0])
            f_name = row[1].split(" ")
            FName.append(f_name[0])
            LName.append(f_name[1])
            DOB.append(datetime.datetime.strptime(row[2], '%Y-%m-%d').strftime('%m/%d/%Y'))
            SSN.append(re.sub(r'\d\d\d-\d\d',r'xxx-xx',row[3]))
            State.append(us_state_abbrev[row[4]])
    
    cleanCSV = zip(EmpID, FName, LName, DOB, SSN, State)

    with open("employee_"+tocheck+".csv", 'w', newline="") as csvFile:

        csvwriter = csv.writer(csvFile, delimiter=',')

        # Write Headers into file
        csvwriter.writerow(["EmpID","First name","Last name","Date of birth","SSN","State"])

        # Write the zipped lists to a csv
        csvwriter.writerows(cleanCSV)

