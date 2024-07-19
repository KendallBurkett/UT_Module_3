import csv

# Path to the CSV file
file_path = '/Users/kendallburkett/Desktop/module_3_challenge/PyBank/Resources/budget_data.csv'

# Initialize variables
total_months = 0
net_total = 0
changes = []
previous_profit_losses = None
greatest_increase = {"date": "", "amount": float('-inf')}
greatest_decrease = {"date": "", "amount": float('inf')}

# Read the CSV file
with open(file_path, 'r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        date = row['Date']
        profit_losses = int(row['Profit/Losses'])
        
        # Calculate the total number of months
        total_months += 1
        
        # Calculate the net total amount of "Profit/Losses"
        net_total += profit_losses
        
        # Calculate changes in "Profit/Losses"
        if previous_profit_losses is not None:
            change = profit_losses - previous_profit_losses
            changes.append(change)
            
            # Check for greatest increase in profits
            if change > greatest_increase['amount']:
                greatest_increase = {"date": date, "amount": change}
            
            # Check for greatest decrease in profits
            if change < greatest_decrease['amount']:
                greatest_decrease = {"date": date, "amount": change}
        
        # Update the previous profit/losses value
        previous_profit_losses = profit_losses

# Calculate the average change
average_change = sum(changes) / len(changes) if changes else 0

# Prepare the results
results = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
)

# Print the results to the terminal
print(results)

# Export the results to a text file
output_file_path = '/Users/kendallburkett/Desktop/module_3_challenge/PyBank/Analysis/financial_analysis.txt'
with open(output_file_path, 'w') as output_file:
    output_file.write(results)
