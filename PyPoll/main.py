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
        # Get the names of each candidate
        name = row[2]  
        if name not in Candidates:
            Candidates[name] = 0
        Candidates[name] += 1

# Calculate the total number of names
total_names = sum(Candidates.values())

# Print the name counts and percentages
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