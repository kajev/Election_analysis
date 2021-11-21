# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of thhe election based on popular vote 

# assign a variable for the file to load and the path

import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0

candidate_options = []

candidate_votes = {}

winning_count = 0
winning_percentage = 0
# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_load) as election_data:


    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    
    for row in file_reader:
        total_votes += 1

        candidate_name = row[2]
        if candidate_name not in candidate_options:

            candidate_options.append(row[2])

            candidate_votes[candidate_name] = 1
        else:
            candidate_votes[candidate_name] += 1
    for candidate_name in candidate_votes:
        #retrieve the vote count of a candidate
        votes = candidate_votes[candidate_name] 
        #calculate the percentage of votes
        vote_percentage = round(float(votes) / float(total_votes) * 100, 2)
        #print the candidate name and percentage of votes
        #print(f" {candidate_name}: received {vote_percentage}% of the vote")
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage

            winning_candidate = candidate_name
    #print(f" {winning_candidate}: {winning_percentage}% ({winning_count})")
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)

