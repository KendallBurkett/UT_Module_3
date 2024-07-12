import csv

file_path = '/Users/kendallburkett/Desktop/module_3_folder/module_3_challenge/PyBank/Resources/budget_data.csv'

total_months = 0
net_total = 0
changes = []
previous_profit_losses = None
greatest_increase = {"date": "", "amount": float('-inf')}
greatest_decrease = {"date": "", "amount": float('inf')}

with open(file_path, 'r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        date = row['Date']
        profit_losses = int(row['Profit/Losses'])
        
        total_months += 1
        
        net_total += profit_losses
        
        if previous_profit_losses is not None:
            change = profit_losses - previous_profit_losses
            changes.append(change)
            
            if change > greatest_increase['amount']:
                greatest_increase = {"date": date, "amount": change}
            
            if change < greatest_decrease['amount']:
                greatest_decrease = {"date": date, "amount": change}
        
        previous_profit_losses = profit_losses

average_change = sum(changes) / len(changes) if changes else 0

results = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
)

print(results)

output_file_path = '/Users/kendallburkett/Desktop/module_3_folder/module_3_challenge/PyBank/Analysis/financial_analysis.txt'
with open(output_file_path, 'w') as output_file:
    output_file.write(results)
