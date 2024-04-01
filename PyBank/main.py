# Import Modules
import os
import csv

# Define the file path name
file_path = os.path.join("Resources","budget_data.csv")

# Open CSV File
with open(file_path, mode = "r", encoding = "UTF-8") as csv_file:
    
    # Define reader variable
    reader = csv.reader(csv_file)

    # Skip the first row (header data)
    data_header = next(reader)

    # Stored the cvs file data into lists
    months = []
    profit_loss = []
    for row in reader:
        months.append(row[0])
        profit_loss.append(int(row[1]))

# Financial Analysis
total_months = len(months)
total_amount = sum(profit_loss)
monthly_changes = [profit_loss[i+1]-profit_loss[i] for i in range(len(profit_loss)-1)]
average_change = round(sum(monthly_changes)/len(monthly_changes),2)
greatest_increase = {"Month": months[monthly_changes.index(max(monthly_changes))+1], "Profit/Loss": max(monthly_changes)}
greatest_decrease = {"Month": months[monthly_changes.index(min(monthly_changes))+1], "Profit/Loss": min(monthly_changes)}

# Summary of Financial Analysis in Terminal
print(
    "Financial Analysis \n"
    "------------------------------------------------- \n"
    f"Total Months: {total_months} \n"
    f"Total: ${total_amount} \n"
    f"Average Change: ${average_change} \n"
    f"Greatest Increase in Profits: {greatest_increase['Month']} (${greatest_increase['Profit/Loss']}) \n"
    f"Greatest Decrease in Profits: {greatest_decrease['Month']} (${greatest_decrease['Profit/Loss']})"
)

# Summary of Financial Analysis in Text File
txt_file_path = os.path.join("analysis", "results.txt")
with open(txt_file_path, "w") as txt_file:
    txt_file.write(
        "Financial Analysis \n"
        "------------------------------------------------- \n"
        f"Total Months: {total_months} \n"
        f"Total: ${total_amount} \n"
        f"Average Change: ${average_change} \n"
        f"Greatest Increase in Profits: {greatest_increase['Month']} (${greatest_increase['Profit/Loss']}) \n"
        f"Greatest Decrease in Profits: {greatest_decrease['Month']} (${greatest_decrease['Profit/Loss']})"
    )