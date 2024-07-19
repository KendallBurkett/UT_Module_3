import csv

file_path = '/Users/kendallburkett/Desktop/module_3_challenge/PyPoll/Resources/election_data.csv'

total_votes = 0
candidates = {}
winner = {"name": "", "votes": 0}

with open(file_path, 'r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        candidate = row['Candidate']
        
        total_votes += 1
        
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    candidates[candidate] = (votes, percentage)
    
    if votes > winner["votes"]:
        winner = {"name": candidate, "votes": votes}

results = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)
for candidate, (votes, percentage) in candidates.items():
    results += f"{candidate}: {percentage:.3f}% ({votes})\n"
results += (
    "-------------------------\n"
    f"Winner: {winner['name']}\n"
    "-------------------------\n"
)

print(results)

output_file_path = '/Users/kendallburkett/Desktop/module_3_challenge/PyPoll/Analysis/election_results.txt'
with open(output_file_path, 'w') as output_file:
    output_file.write(results)
