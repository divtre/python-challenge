import csv
import os

csv_no=['1','2']

for tocheck in csv_no :
    pybank_csv = os.path.join('raw_data', 'budget_data_' + tocheck+'.csv')
    # Read the csv and convert it into a list of dictionaries
    with open(pybank_csv) as revenue_data:
        reader = csv.reader(revenue_data)

        # use of next to skip first title row in csv file
        next(reader) 
        revenue = []
        date = []
        rev_change = [] 

        for row in reader:
            revenue.append(float(row[1]))
            date.append(row[0])
        var1=len(date)
        var2=sum(revenue)
        print("Financial Analysis")
        print("-----------------------------------")
        print("Total Months:", len(date))
        print("Total Revenue: $", sum(revenue))

        for i in range(1,len(revenue)):
            #print("uuu"+str(revenue[1])+"***"+str(revenue[0]))
            rev_change.append(revenue[i] - revenue[i-1])   

            max_rev_change = max(rev_change)

            min_rev_change = min(rev_change)
            index=rev_change.index(max_rev_change)+1
            index_2=rev_change.index(min_rev_change)+1
            max_rev_change_date = str(date[index])
            min_rev_change_date = str(date[index_2])

        avg_rev_change = (sum(rev_change)+revenue[0])/(len(rev_change)+1)

        print("Average Revenue Change: $", round(avg_rev_change))
        print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
        print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")

        output_path = os.path.join('output_budget_data_' +tocheck+'.txt')
        file = open(output_path, 'w')
        file.write("Financial Analysis \n") 
        file.write("-----------------------------------\n")
        file.write("Total Months: "+str(var1)+"\n")
        file.write("Total Revenue: "+str(var2)+"\n")
        file.write("Average Revenue Change: $"+str(round(avg_rev_change))+"\n")
        file.write("Greatest Increase in Revenue: "+str(max_rev_change_date)+"($"+ str(max_rev_change)+")"+"\n")
        file.write("Greatest Decrease in Revenue: "+str(min_rev_change_date)+"($"+ str(min_rev_change)+")"+"\n")


        file.close()
          