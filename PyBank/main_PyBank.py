##########################
#       Homework 3       #
# Student: Matheus Gratz #
# Introduction to Python #
##########################

#import modules
import os
import csv

# define the path to the csv file and txt output file
csvpath = os.path.join("Resources", "budget_data.csv")
txtpath = os.path.join("Analysis", "output_analysis.txt")

#check if the file exists. If YES, remove it. If no, create a new one.
if os.path.exists(txtpath):
  os.remove(txtpath)
else:
  open(txtpath, 'a').close()

# read the csv file
with open(csvpath, encoding="utf-8-sig") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader, None) #dismiss headers

# Create variables
    total = 0.0      
    count = 0
    profit_losses = []

    total_diff = 0
    average_diff = 0.00
    gtProfitValue = 0
    gtProfitMonth = ""
    gtLossValue = 0
    gtLossMonth = ""

# Loop through rows
    for row in csvreader:
        total += float(row[1])              #Calculate Total Profit/Losses
        count += 1                          #Calculate number of months
        profit_losses.append(row)           #Generate list
    
#Loop profit/losses list and look for increase/decrease 
# and calculate differences
    for i in range(1, count, 1):           
      diff = int(profit_losses[i][1]) - int(profit_losses[i-1][1])
      total_diff = total_diff + diff

#Test and set Greatest increase in profits
      if diff > gtProfitValue:     
          gtProfitValue = diff
          gtProfitMonth = profit_losses[i][0]

#Test and set Greatest decrease in losses
      if diff < gtLossValue:
          gtLossValue = diff
          gtLossMonth = profit_losses[i][0]

average_diff = total_diff / (count-1)

#Print analysis and write file
print(f"""
Financial Analisys
---------------------------
Total Months: {count}
Total: ${round(total)}
Average Change: ${round(average_diff,2)}
Greatest Increase in Profits: {gtProfitMonth} (${gtProfitValue})
Greatest Decrease in Profits: {gtLossMonth} (${gtLossValue})
---------------------------
""", file=open(txtpath, 'a'))

txt = open(txtpath, 'r')
txt_content = txt.read()
print(txt_content)
txt.close()