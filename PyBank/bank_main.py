import os
import csv

csv_no=['1','2']

for tocheck in csv_no :
    pybank_csv = os.path.join('raw_data', 'budget_data_' + tocheck+'.csv')
    with open(pybank_csv, 'r', encoding="utf-8") as csvFile:
        Date=[]
        Revenue=[]
        csvReader = csv.reader(csvFile, delimiter=',')

        # Skipp headers
        next(csvReader, None)
        
        for row in csvReader:

            # Append data from the row
            Date.append(row[0])
            Revenue.append(row[1])
            no_of_months=len(Date)
            total_revenue=0
            total_revenue=int(total_revenue)+(int(row[1]))
            avg_revenue=int(total_revenue)/int(no_of_months)
            max_revenue_row = max(Revenue, key=int)
            min_revenue_row= min(Revenue,key=int)
          
            max_date_index=int(Revenue.index(max_revenue_row))
            min_date_index=int(Revenue.index(min_revenue_row))
            
            max_date=Date[max_date_index]
            min_date=Date[min_date_index]
        print("Financial Analysis")
        print("---------------------")
        print("Total no of months : "+str(no_of_months))
        print("Total Revenue : "+str(total_revenue))
        print("Average Revenue :"+str(avg_revenue))
        print("Greated increase in revenue: "+str(max_date)+" "+"("+str(max_revenue_row)+")")
        print("Greated decrease in revenue: "+str(min_date)+" "+"("+str(min_revenue_row)+")")
        #print("##"+str(max_date_index))
        #print("max revenue"+str(max_revenue_row)+" "+str(max_date))