# Import and Read from file
import os
import csv


Budget_data_path = os.path.join("Resources", "budget_data.csv")

profits = 0
losses = 0
total_months=0
total_net =0
previous_data=0
net_change_list = []
change=0
greatest_increase =["",0]
greatest_decrease =["",9999999999]



with open(Budget_data_path, "r") as Budget_data:
    Budget_data_reader = csv.reader(Budget_data, delimiter=",")
    # skip header
    header=next(Budget_data_reader)
    jan_data= next(Budget_data_reader)
    total_months= total_months+1
    total_net=total_net+int(jan_data[1])
    previous_data=int(jan_data[1])

    for row in Budget_data_reader:
        total_months= total_months+1
        total_net=total_net+int(row[1])
        change=int(row[1])-previous_data
        previous_data=int(row[1])

        net_change_list=net_change_list+[change]
        if change > greatest_increase[1]:
            greatest_increase[1]=change
            greatest_increase[0]=row[0]

        if change < greatest_decrease[1]:
            greatest_decrease[1]=change
            greatest_decrease[0]=row[0]
        
average_change= sum(net_change_list)/len(net_change_list)

print (total_months)
print (total_net)
print (round(average_change,2))
print (greatest_increase[0],greatest_increase[1])
print (greatest_decrease[0],greatest_decrease[1])
