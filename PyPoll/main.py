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

voterCast=[]

voterTally = {}

csvpath = './Resources/election_data.csv'
output_file = './analysis/election_results.csv'

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
#print(totalVotes)

filteredCandidates = set(voterCast)

#I know there is a built in function "from collections import counter" that would do what I need.  Wanted to learn more.

for candidate in filteredCandidates:
     voterTally[candidate] = [0,0]
    
for candidate in filteredCandidates:
    for vote in voterCast:
        if candidate == vote:
         voterTally[candidate][1] = int(voterTally[candidate][1]) + 1
    voterTally[candidate][0] = round(float(100 * voterTally[candidate][1] / totalVotes),3)
#for candidate in voterTally:

voterTally = {k: v for k, v in sorted(voterTally.items(), key = lambda item: item[1], reverse = True)}

with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile, delimiter=' ')
    printScreenFile("Election Results")
    printScreenFile("--------------------------------")
    printScreenFile(f"Total Votes: {totalVotes}")
    printScreenFile("--------------------------------")
    for candidate in voterTally.keys():
        printScreenFile(f"{candidate}: {voterTally[candidate][0]} % ({voterTally[candidate][1]})")
    printScreenFile("--------------------------------")

    printScreenFile(f"Winner: {list(voterTally)[0]}")

    printScreenFile("--------------------------------")


#now to sort the condidates by vote %

#This returns a list.  Don't want that.
#voterTally = [(key, value) for (key, value) in sorted(voterTally.items(), key = lambda x: x[1], reverse = True )]
#voterTally = [k: v for k, v in sorted(voterTally.items(), key = lambda item: item[1])]

#below gives a tuple.  Don't want that.
#voterTally = sorted(voterTally.items(), key = lambda item: item[1], reverse = True)