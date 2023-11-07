import os
import csv

# Set path for file
CSV_PATH = os.path.join("Resources", "budget_data.csv")
analysis_PATH = os.path.join("analysis", "analysis.txt")
#os.chdir(os.path.dirname(os.path.realpath(__file__)))
counter = 0
total_pl = 0
Total_Changes = 0
Previous_PL = 0
Max_Increase = 0
Max_Month = ""
Min_ = 0
Min_Month = ""
# Open the CSV using the UTF-8 encoding
with open(CSV_PATH, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile)

    #skip the row heder
    header = next(csvreader)
    
    
    # Loop through changes in the P/L
    for row in csvreader:
       #print(f'Date: {row[0]}, P&L: {row[1]}')
       counter = counter + 1
       # calculate total P&L
       total_pl = total_pl + int(row[1])
       if counter > 1:
           change_PL = int(row[1]) - Previous_PL
           Total_Changes = Total_Changes + change_PL
           if change_PL > Max_Increase: 
               Max_Increase = change_PL
               Max_Month = row[0]
           if change_PL < Min_:
               Min_ = change_PL
               Min_Month = row[0]
       Previous_PL = int(row[1])
               
#average of those changes        
average_change = Total_Changes/(counter-1)
       
print(f'Financial Analysis')
print(f'-------------------------')
print(f'Total Months: {counter}')
print(f'Total P&L: {total_pl}')
print(f'Average Change:{average_change}') 
print(f'Greatest Increase in Profits:{Max_Month}(${Max_Increase})')
print(f'Greatest Decrease in Profits:{Min_Month} (${Min_})')

analysis_PATH = os.path.join("analysis", "analysis.txt")

with open(analysis_PATH, 'w') as textfile:
    
    textfile.write(f'Financial Analysis\n')
    textfile.write(f'-------------------------\n')
    textfile.write(f'Total Months: {counter}\n')
    textfile.write(f'Total P&L: {total_pl}\n')
    textfile.write(f'Average Change:{average_change}\n')      
    textfile.write(f'Greatest Increase in Profits:{Max_Month}(${Max_Increase})\n')
    textfile.write(f'Greatest Decrease in Profits:{Min_Month} (${Min_})')



   





             


       




                     