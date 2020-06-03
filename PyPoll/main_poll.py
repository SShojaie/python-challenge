# Import modules
import os
import csv
import operator
import sys

csvpath = os.path.join('Resources','election_data.csv')

# Define a function for the poll analysis

def poll_analysis(poll_data):
  
    print ("\nElection Results \n----------------------------")
    
    # Analysis
    total_votes = len(poll_data)
    print (f"Total Votes: {(total_votes)} \n----------------------------")


    candidates_list = []
    votes_count_dict = {}
    votes_percentage_dict = {}
    
    for row in poll_data:
        candidate = row[2]
        if candidate not in candidates_list:
            candidates_list.append(candidate)

    for curr_candidate in candidates_list:
        votes_count_dict[curr_candidate] = 0
        votes_percentage_dict[curr_candidate] = 0

    for row in poll_data:
        candidate = row[2]
        votes_count_dict[candidate] += 1

    for curr_candidate in candidates_list:
        votes_percentage_dict[curr_candidate] = votes_count_dict[curr_candidate] / total_votes
   
    for tally in candidates_list:
            print (f"{tally}: {'{:.3%}'.format(votes_percentage_dict[tally])} ({votes_count_dict[tally]})") 
    print ("----------------------------")

    # Find the winner
    winner = max(votes_percentage_dict, key=votes_percentage_dict.get)
    print(f"Winner: {winner}\n----------------------------")        


# Read in the CSV file
with open(csvpath, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    data = []

    # Populating data
    for row in csvreader:
        data.append(row)

    poll_analysis(data)


# Export to txt file
output_path = os.path.join("Analysis", "Analysis.txt")

sys.stdout=open(output_path,"w")
poll_analysis(data)  






