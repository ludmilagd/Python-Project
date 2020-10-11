# Import and Read from file
import os
import csv


election_data_path = os.path.join("Resources", "election_data.csv")


candidate_name =[]
candidate_votes={}
total_votes =0
percent = []

with open(election_data_path, "r") as election_data:
    election_data_reader = csv.reader(election_data, delimiter=",")

    header= next(election_data_reader)

    for row in election_data_reader:
        candidate_name= row[2]
        if candidate_name in candidate_votes.keys():
            candidate_votes [candidate_name]= candidate_votes [candidate_name]+1

        else:
            candidate_votes [candidate_name]=1

        
total_votes= sum(candidate_votes.values())
print (total_votes)
for i in candidate_votes:

    percent = round((candidate_votes[i]/total_votes)*100,0)

    print (f'{i} {percent} {candidate_votes[i]}')

for key in candidate_votes.keys():
    if candidate_votes [key]== max(candidate_votes.values()):
        winner=key

print (winner)


