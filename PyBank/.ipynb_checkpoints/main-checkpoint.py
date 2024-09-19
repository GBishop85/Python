import csv

 
#joining path
budget_data = Path("Resources", "budget_data.csv")


# Retrieve Budget Data from CSV file
with open('budget_data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row

# find net amount of profit and loss
P = []
months = []

 #read through each row of data after header
for rows in:
P.append(int(rows[1]))
months.append(rows[0])

<<<<<<< HEAD
    # find revenue change
revenue_change = []
=======
    # find revenue 
    revenue_change = []
>>>>>>> 3c5303d8c565cffeb6d56b57b41bff1d27ed5a4b

for x in range(1, len(P)):
        revenue_change.append((int(P[x]) - int(P[x-1])))
    
    # calculate average revenue change
revenue_average = sum(revenue_change) / len(revenue_change)
    
<<<<<<< HEAD
    # calculate total length of months
total_months = len(months)
=======
    # total length of months
    total_months = len(months)
>>>>>>> 3c5303d8c565cffeb6d56b57b41bff1d27ed5a4b

    # greatest increase in revenue
greatest_increase = max(revenue_change)
    # greatest decrease in revenue
greatest_decrease = min(revenue_change)


    # print the Results
<<<<<<< HEAD
print("Financial Analysis")
=======
    print("Financial Analysis")
>>>>>>> 3c5303d8c565cffeb6d56b57b41bff1d27ed5a4b

print("....................................................................................")

print("total months: " + str(total_months))

print("Total: " + "$" + str(sum(P)))

print("Average change: " + "$" + str(revenue_average))

print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))

print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))


    # output to a text file

file = open("output.txt","w")

file.write("Financial Analysis" + "\n")

file.write("...................................................................................." + "\n")

file.write("total months: " + str(total_months) + "\n")

file.write("Total: " + "$" + str(sum(P)) + "\n")

file.write("Average change: " + "$" + str(revenue_average) + "\n")

file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase) + "\n")

file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease) + "\n")

file.close()