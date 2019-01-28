import os
import csv

months = []
total_profit_loss = 0
greatest_profit_date = []
greatest_profit_amount = 0
greatest_loss_date = []
greatest_loss_amount = 0

csvpath = os.path.join('budget_data.csv')

with open(csvpath,newline='') as csvfile:

    csvreader = csv.reader(csvfile,delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        months.append(row[0])
        total_profit_loss = int(row[1]) + int(total_profit_loss)
        if int(row[1]) > int(greatest_profit_amount):
            greatest_profit_date = row[0]
            greatest_profit_amount = row[1]
        if int(row[1]) < int(greatest_loss_amount):
            greatest_loss_date = row[0]
            greatest_loss_amount = row[1]
    #print(len(months), total_profit_loss, greatest_loss_amount, greatest_loss_date, greatest_profit_amount, greatest_profit_date)
        average_profit_loss = total_profit_loss / len(months)
    print("Financial Analysis")
    print("------------------------")
    print(f"Total Months: {len(months)}")
    print(f"Total ${total_profit_loss}")
    print(f"Average Change: ${average_profit_loss}")
    print(f"Greatest Increase in Profits: {greatest_profit_date} ({greatest_profit_amount})")
    print(f"Greatest Decrease in Profits: {greatest_loss_date} ({greatest_loss_amount})")

    output_file = os.path.join("Financial_Analysis.txt")

    with open(output_file,'w') as text:

        text.write("Financial Analysis\n")
        text.write("------------------------\n")
        text.write(f"Total Months: {len(months)}\n")
        text.write(f"Total ${total_profit_loss}\n")
        text.write(f"Average Change: ${average_profit_loss}\n")
        text.write(f"Greatest Increase in Profits: {greatest_profit_date} ({greatest_profit_amount})\n")
        text.write(f"Greatest Decrease in Profits: {greatest_loss_date} ({greatest_loss_amount})\n")



