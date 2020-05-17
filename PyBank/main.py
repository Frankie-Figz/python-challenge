# -*- coding: utf-8 -*-
"""
Created on Wed May 13 20:46:08 2020

@author: theaddies
"""

# Module for reading CSV files
import csv


def printScreenFile(message):
    print(message)
    writer.writerow([message])

financeData=[]

csvpath = './Resources/budget_data.csv'

# Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    financeData.append(csv_header)
    
    # Read each row of data after the header
    for row in csvreader:
        print(row)
        financeData.append(row)
    
        
n = 0
maxProfitIncrease = 0
maxProfitDecrease = 0
totalProfit = 0
profitChange = 0
totalProfitChange = 0

print(financeData)

for row in range(1, len(financeData)):
    financeData[int(row)][1] = int(financeData[int(row)][1])

for row in range(1, len(financeData)):
   totalProfit = totalProfit + financeData[int(row)][1]
   if row <= (len(financeData)-2):
       profitChange = financeData[int(row+1)][1] - financeData[int(row)][1]
       totalProfitChange = totalProfitChange + profitChange
   if maxProfitIncrease< profitChange:
        maxProfitIncrease = profitChange
        increaseDate = int(row)
   if maxProfitDecrease > profitChange:
        maxProfitDecrease = profitChange
        decreaseDate = int(row)
averageChange = totalProfitChange / (len(financeData)-2)

# Set variable for output file
output_file = "./analysis/pyBank.csv"

#  Open the output file
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile, delimiter=' ')
      
    printScreenFile("Financial Analysis")
    printScreenFile("--------------------------------")
    
    printScreenFile(f"Total months: = {str(len(financeData)-1)}")
    printScreenFile(f"Total: = {totalProfit}")
    
    #print(f"Average Change: = {str(averageChange)}")
    
    averageChange = format(averageChange, '.2f')
    
    printScreenFile(f"Average Change: = {averageChange}")
    printScreenFile(f"Greatest Increase in Profits: {financeData[increaseDate][0]} {maxProfitIncrease}")
    printScreenFile(f"Greatest decrease in Profits: {financeData[decreaseDate][0]} {maxProfitDecrease}")


      