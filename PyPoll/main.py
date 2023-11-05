import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")
os.chdir(os.path.dirname(os.path.realpath(__file__)))
# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile)

    #skip the row heder
    header = next(csvreader)
    counter = 0
    
    for row in csvreader:
        counter += 1

    for candidate_name = row[2] 
        

    print(f'Total number of votes cast: {counter}')

      

    
 

   