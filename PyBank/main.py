import csv
import os
 
#joining path
budget_data = os.path.join("Resources", "budget_data.csv")
text_analysis=os.path.join("Analysis","Text_Analysis.txt")

# Retrieve Budget Data from CSV file
with open(budget_data) as file:
    reader = csv.reader(file)
    column_headers=next(reader)  # Skip the header row

# find net amount of profit and loss
    P = []
    months = 1
    first_row=next(reader)
    net_profit=int(first_row[1])
    previous_net=int(first_row[1])
 


#read through each row of data after header
    for rows in reader:
        months+=1
        net_profit+=int(rows[1])
           
        revenue_change=int(rows[1])-previous_net
        previous_net=int(rows[1])
        P.append(revenue_change)
            
            # calculate average revenue change
revenue_average = sum(P) / len(P)

# greatest increase in revenue
greatest_increase = max(P)
            # greatest decrease in revenue
greatest_decrease = min(P)


    # print the Results
output=(f"Financial Analysis\n"

f"....................................................................................\n"

f"total months: {months}\n"

f"Total: ${net_profit}\n"

f"Average change: ${revenue_average}\n"

f"Greatest Increase in Profits: ${greatest_increase}\n"

f"Greatest Decrease in Profits: ${greatest_decrease}\n"
)
print(output)
with open(text_analysis,"w") as output_file:
    output_file.write(output)