##########################
#       Homework 3       #
# Student: Matheus Gratz #
# Introduction to Python #
##########################

#import modules
import os
import csv
from collections import Counter

# define the path to the csv file and the txt output file
csvpath = os.path.join("Resources", "election_data.csv")
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

#Establish variables
    count = 0
    list_candidates = []

#loop through rows
    for row in csvreader:
        count += 1
        list_candidates.append(row[2])

#generate summary of rows
    summary = Counter(list_candidates)

#Print summary and write into a file
    print("Election Results", file=open(txtpath, 'a'))
    print("---------------------------", file=open(txtpath, 'a'))
    print(f"Total Votes: {count}", file=open(txtpath, 'a'))
    print("---------------------------", file=open(txtpath, 'a'))

#loop through data       
    for candidate in summary.keys():
        name = candidate
        percentage = round(summary[candidate] / count * 100 , 3)
        total_votes = summary[candidate]
        print(f"{name}: {percentage}% ({total_votes})", file=open(txtpath, 'a'))
    
    print("---------------------------", file=open(txtpath, 'a'))
    print(f"Winner: {list(summary.keys())[0]}", file=open(txtpath, 'a'))
    print("---------------------------", file=open(txtpath, 'a'))

txt = open(txtpath, 'r')
txt_content = txt.read()
print(txt_content)
txt.close()