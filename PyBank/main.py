import csv
with open("bankdata.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #  with open('bankdata.csv','w') as new_file:
    #      csvwriter = csv.writer(new_file)
    next(csvreader)
    totalmonths = 0
    total = 0
    profloss = [] #
    for row in csvreader:
      month = row[0]
      totalmonths = totalmonths+1
      total +=int(row[1])
      profloss.append(int(row[1]))
    # print(totalmonths)
    # print(total)
    # print(profloss)
    difference = []     # created a new array of differences
    current_month = 0
    previous_month = 0
    for value in profloss:  # Loop thrugh all values of x
      current_month = int(value)
      difference.append(current_month - previous_month) #adding the values in "difference" list
      previous_month = current_month
    average_change= sum(difference)/len(difference)
   
    print("Financial Analysis")
    print("---------------------------------")
    print("Total months : " + str(totalmonths))
    print("Average change : " + str(round(average_change,2)))
    print("Greatest Increase in Profits: $" + str(max(difference)))
    print("Greatest Decrease in Profits: $" + str(min(difference)))
    
    #run this command: python main.py >> results.txt

