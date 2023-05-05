# Python-Challenge
Module 3

#In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. 
#______You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".
#Your task is to create a Python script that analyzes the records to calculate each of the following values:
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period
#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
#------------------------------------------------------------------------------------------------------------------------------------------------\

#import OS module to allow to allow to create file paths between operating systems 
import os

#module for reading .csv files
import csv 
csvpath = os.path.join('Resources','budget_data.csv')

#Output date
Months = 0
Total = 0
Profit_Loss_Values = []
PreviousProfit = 0
GreatestIncrease = 0
GreatestIncreaseDate = ""
GreatestDecrease = 0
GreatestDecreaseDate = ""

with open(csvpath) as csvfile:
    #CSV Reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter =",")
    

    #skip the header row 
    next(csvreader)
    
    #loop thru all the rows in the file
    for row in csvreader:
       #calculating the total number of months
        Months += 1
        #calculating the total
        Total += float(row[1])
        #creating a list of the values under the profit and loses column
        Profit_Loss_Values.append(int(row[1]))

        #Getting the current value of the profit and calculating the change to the previous value
        CurrentProfit = float(row[1])
        Change = CurrentProfit - PreviousProfit 
        #Calculating greatest increase and corresponding date
        if Change > GreatestIncrease:
            GreatestIncrease = Change
            GreatestIncreaseDate = row[0]
        PreviousProfit = CurrentProfit

        #Calculating greates Decrease and corresponding date
        if Change < GreatestDecrease:
            GreatestDecrease = Change
            GreatestDecreaseDate = row[0]
       
 #calculate average change
average_change = sum(Profit_Loss_Values[i+1] - Profit_Loss_Values[i] for i in range(len(Profit_Loss_Values)-1))/(len(Profit_Loss_Values)-1)   

#Terminal outputs
print(f"Financial Analysis")
print(f"---------------------------------------")
print(f"Total Months: {Months}")
print(f"Total: {Total}")
print(f'Average Change: {average_change:.2f}')
print(f'Greatest Increase in Profits : {GreatestIncreaseDate} (${GreatestIncrease:.2f})')
print(f'Greatest Decrease in Profits : {GreatestDecreaseDate} (${GreatestDecrease:.2f})')

#text file outputs 
output_path = os.path.join("Analysis","Financial Analysis.txt")
with open(output_path, "w") as file:
    file.write("Financial Analysis\n")
    file.write("---------------------------------------\n")
    file.write(f"Total Months: {Months}\n")
    file.write(f"Total: {Total}\n")
    file.write(f"Average Change: {average_change:.2f}\n")
    file.write(f'Greatest Increase in Profits : {GreatestIncreaseDate} (${GreatestIncrease:.2f})\n')
    file.write(f'Greatest Decrease in Profits : {GreatestDecreaseDate} (${GreatestDecrease:.2f})\n')

------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------


#In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
#You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
#Your task is to create a Python script that analyzes the votes and calculates each of the following values:
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote

#import OS module to allow to allow to create file paths between operating systems 
import os

#module for reading .csv files
import csv 
csvpath = os.path.join('Resources','election_data.csv')

TotalVotes = 0
Candidates = {}
with open(csvpath) as csvfile:
    #CSV Reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter =",")

    #skip the header row
    next(csvreader)

    #loop thru all the rows in the file
    for row in csvreader:
        #calculate the total number of votes
        TotalVotes += 1
        # Get the names of each candidate and increase count every time a candidate is repeated
        name = row[2]  
        if name not in Candidates:
            Candidates[name] = 0
        Candidates[name] += 1

# Calculate the total number of names
total_names = sum(Candidates.values())

# Print the name counts for each candidate and percentages
for name, count in Candidates.items():
    percentage = (count / total_names) * 100   


print("Election Results")
print("----------------------------------------")
print(f'Total Votes: {TotalVotes}')
print("----------------------------------------")
#print out each candidate with the vote count and percentage of votes
for name, count in Candidates.items():
    percentage = (count / total_names) * 100   
    print(f'{name}: {count} ({percentage:.2f}%)')
print("----------------------------------------")

# get the winning candidate and print
winner = max(Candidates, key=Candidates.get)
print(f'Winner: {winner}')
print("----------------------------------------")

#text file outputs to the Analysis folder
output_path = os.path.join("Analysis","Election Results.txt")
with open(output_path, "w") as file:
    file.write("Election Results\n")
    file.write("----------------------------------------\n")
    file.write(f"Total Votes: {TotalVotes}\n")
    file.write("----------------------------------------\n")
    #print out each candidate with the vote count and percentage of votes
    for name, count in Candidates.items():
        vote_percentage = count / total_names * 100
        file.write(f"{name}: {percentage:.2f}% ({count})\n")
    file.write("----------------------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("----------------------------------------\n")

