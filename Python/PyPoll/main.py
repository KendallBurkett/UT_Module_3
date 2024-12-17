import csv

# Path to the CSV file
file_path = '/Users/kendallburkett/Desktop/module_3_folder/module_3_challenge/PyPoll/Resources/election_data.csv'

# Initialize variables
total_votes = 0
candidates = {}
winner = {"name": "", "votes": 0}

# Read the CSV file
with open(file_path, 'r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        candidate = row['Candidate']
        
        # Calculate the total number of votes
        total_votes += 1
        
        # Calculate the total number of votes each candidate won
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Calculate the percentage of votes each candidate won
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    candidates[candidate] = (votes, percentage)
    
    # Determine the winner of the election based on popular vote
    if votes > winner["votes"]:
        winner = {"name": candidate, "votes": votes}

# Prepare the results
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

# Print the results to the terminal
print(results)

# Export the results to a text file
output_file_path = '/Users/kendallburkett/Desktop/module_3_folder/module_3_challenge/PyPoll/Analysis/election_results.txt'
with open(output_file_path, 'w') as output_file:
    output_file.write(results)
