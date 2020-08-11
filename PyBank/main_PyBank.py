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

    gtProfitValue = 0
    gtProfitMonth = ""
    gtLossValue = 0
    gtLossMonth = ""

# Loop through rows
    for row in csvreader:
        total += float(row[1])              #Calculate Total Profit/Losses
        count += 1                          #Calculate number of months
        mean = total/count                  #Calculate average

#Test and set Greatest increase in profits
        if int(row[1]) > gtProfitValue:     
            gtProfitValue = int(row[1])
            gtProfitMonth = row[0]

#Test and set Greatest decrease in losses
        if int(row[1]) < gtLossValue:
            gtLossValue = int(row[1])
            gtLossMonth = row[0]


# Print analysis and write file
print(f"""
Financial Analisys
---------------------------
Total Months: {count}
Total: ${total}
Average Change: ${round(mean,2)}
Greatest Increase in Profits: {gtProfitMonth} (${gtProfitValue})
Greatest Decrease in Profits: {gtLossMonth} (${gtLossValue})
---------------------------
""", file=open(txtpath, 'a'))

txt = open(txtpath, 'r')
txt_content = txt.read()
print(txt_content)
txt.close()