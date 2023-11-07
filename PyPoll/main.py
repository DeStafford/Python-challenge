import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")
#os.chdir(os.path.dirname(os.path.realpath(__file__)))
textpath = os.path.join("analysis", "election_results.txt")
#Initialize a dictionary to store candidate votes
candidate_votes = {}

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile)
 
    #skip the row heder
    header = next(csvreader)
    counter = 0

# count number of votes 
    total_votes = 0  
    
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2] 

#update directory 
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1 
        else:
            candidate_votes[candidate_name] = 1 

with open(textpath,'w', encoding='UTF-8') as textfile:              
    #print out the total numbeer of votes cast
    print(f'Election Results')
    print(f'-------------------------')
    print(f'Total Votes: {total_votes}')
    print(f'-------------------------')

    textfile.write(f'Election Results\n')
    textfile.write(f'-------------------------\n')
    textfile.write(f'Total Votes: {total_votes}\n')
    textfile.write(f'-------------------------\n')

    # Define used to calulate_percentage function 
    def calculate_percentage(candidate_votes, total_votes):
        percentages = {}
        for candidate, votes in candidate_votes.items():
            percentage = (votes / total_votes) * 100
            percentages[candidate] = percentage 
        return percentages

    #calulate percentatages
    percentages = calculate_percentage(candidate_votes, total_votes)

    #Print out percentages 
    for candidate, percentage in percentages.items():
        print(f'{candidate}: {percentage:.2f}% ({candidate_votes[candidate]} votes) ' )
        textfile.write(f'{candidate}: {percentage:.2f}% ({candidate_votes[candidate]} votes)\n ' )
    #Determine the winner 
    winner = max(percentages, key=percentages.get)
    print(f'-------------------------')
    print(f'Winner: {winner}')
    print(f'-------------------------')

    textfile.write(f'-------------------------\n')
    textfile.write(f'Winner: {winner}\n')
    textfile.write(f'-------------------------\n')
        
                                    
        
    

      

    
 

   