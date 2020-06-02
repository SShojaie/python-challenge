# Import modules
import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')

#Define a function for the financial analysis

def financial_analysis(budget_data):
  
    print ("Financial Analysis \n----------------------------")
    
    #Analysis
    
    total_months = len(budget_data)
    print (f"Total Months: {(total_months)}")
    
    total_net = 0
    for row in budget_data:
        total_net += int(row[1])
    print (f"Total: ${total_net}")

    i = 0
    total_change = 0

    greatest_increase = None
    greatest_decrease = None
    increase_date = None
    decrease_date = None

    while i < len(budget_data)-1:
        change = int(budget_data[i+1][1]) - int(budget_data[i][1])
        total_change += change

        if change > 0: # An increase
            if greatest_increase == None: # First increase
                greatest_increase = change
                increase_date = budget_data[i+1][0]
            else:
                if change > greatest_increase:
                    greatest_increase = change
                    increase_date = budget_data[i+1][0]

        elif change < 0: # A decrease
            if greatest_decrease == None: # First increase
                greatest_decrease = change
                decrease_date = budget_data[i+1][0]
            else:
                if change < greatest_decrease:
                    greatest_decrease = change
                    decrease_date = budget_data[i+1][0]
  
        i += 1
        average_change = round(total_change/(total_months-1),2)

    print (f"Average Change: ${(average_change)}")
    print ("Greatest Increase in Profits: "+ increase_date +" ($" + str(greatest_increase) +")")
    print ("Greatest Decrease in Profits: "+ decrease_date +" ($" + str(greatest_decrease) +")")












# Read in the CSV file
with open(csvpath, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    data = []

    # Populating data
    for row in csvreader:
        data.append(row)

    financial_analysis(data)






#Financial Analysis Output: 

#print ("Financial Analysis")
#print ("----------------------------")



