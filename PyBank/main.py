# Import Resources
import os
import csv

#Set File Path
csvpath = os.path.join( 'Resources', 'budget_data.csv')

#Open 
with open(csvpath, newline='') as csvfile:

# Read File
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #Set initial values in variable before file read loop
    
    total_pl = 0
    greatest_profit_inc = 0
    greatest_profit_dec = 0
    total_change = 0
    total_months = 0
    prev_mth_profit = 0

    # Read each row of data after the header
    for row in csvreader:
        total_months += 1
       
        total_pl = total_pl + int(row[1])
        
        change = int(row[1]) - prev_mth_profit
        #print(f"Change : {str(change)} current: {str(row[1])} Previous: {str(prev_mth_profit)}")
        #Calculate period with geatest profit increas)e
        if  int(row[1]) > prev_mth_profit and change > greatest_profit_inc:
            #print(f" Increase : {row[0]} {row[1]} Previous: {str(prev_mth_profit)}")
            greatest_profit_inc_pd= row[0]
            greatest_profit_inc = change
         #Calculate period with geatest profit increase
        
        if int(row[1]) < prev_mth_profit and change < greatest_profit_dec:
            #print(f" deccrease : {row[0]} {row[1]} Previous: {str(prev_mth_profit)}")
            
            greatest_profit_dec_pd = row[0]
            greatest_profit_dec = change

        if total_months > 1:
            total_change = total_change + change
    
        prev_mth_profit = int(row[1])
        
    average_change = round(total_change/(total_months-1),2)

    print(f"Total Months {str(total_months)}")
    print(f"Total Profit/Loss {str(total_pl)}")
    print(f"Average Change $ {str(average_change)}")
    print(f"Greatest Increase in Profits: {greatest_profit_inc_pd}  ($ {str(greatest_profit_inc)} )")
    print(f"Greatest Decrease in Profits: {greatest_profit_dec_pd}  ($ {str(greatest_profit_dec)} )")

#Write output to Text file

import sys
with open('budget_summary.txt', 'w') as f:
    sys.stdout = f
    print(f"Total Months {str(total_months)}")
    print(f"Total Profit/Loss {str(total_pl)}")
    print(f"Average Change $ {str(average_change)}")
    print(f"Greatest Increase in Profits: {greatest_profit_inc_pd}  ($ {str(greatest_profit_inc)} )")
    print(f"Greatest Decrease in Profits: {greatest_profit_dec_pd}  ($ {str(greatest_profit_dec)} )")