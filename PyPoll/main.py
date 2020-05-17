# -*- coding: utf-8 -*-
"""
Created on Wed May 13 20:46:08 2020

@author: theaddies
"""

# Module for reading CSV files
import csv

voterCast=[]

voterTally = {}

csvpath = './Resources/election_data.csv'

# Improved Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

#    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    next(csvreader,None)
#    print("vote")
    
#    voterCast.append("Candidate")
    
    # Read each row of data after the header
    for row in csvreader:
        voterCast.append(row[2])

totalVotes = len(voterCast)
print(totalVotes)

filteredCandidates = set(voterCast)

#I know there is a built in function "from collections import counter" that would do what I need.  Wanted to learn more.

for candidate in filteredCandidates:
     voterTally[candidate] = 0
    
for vote in voterCast:
    for candidate in filteredCandidates:
#        voterTally[candidate] = 0
        if candidate == vote:
         voterTally[candidate] = voterTally[candidate] + 1
         
