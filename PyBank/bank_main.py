import os
import csv

csv_no=['1','2']

for tocheck in csv_no :
    pybank_csv = os.path.join('raw_data', 'budget_data_' + tocheck+'.csv')
    with open(pybank_csv, 'r', encoding="utf-8") as csvFile:
        Date=[]
        Revenue=[]
        Revenue_increase=[]
        total_revenue=0
        csvReader = csv.reader(csvFile, delimiter=',')

        # Skipp headers
        next(csvReader, None)
        
        for row in csvReader:

            # Append data from the row
            Date.append(row[0])
            Revenue.append(row[1])
            no_of_months=len(Date)
            print
            print("Financial Analysis")
            print("-----------------------------------")
            print("Total Months:", no_of_months)
            print("Total Revenue: $", sum(Revenue))

            for i in range(0,no_of_months+1):
                rev_change.append(revenue[i] - revenue[i-1])   
                avg_rev_change = sum(rev_change)/len(rev_change)

                max_rev_change = max(rev_change)

                min_rev_change = min(rev_change)

                max_rev_change_date = str(date[rev_change.index(max(rev_change))])
                min_rev_change_date = str(date[rev_change.index(min(rev_change))])


    print("Avereage Revenue Change: $", round(avg_rev_change))
    print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
    print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")