import csv
from datetime import datetime
import time


input_file = 'input.csv'
output_file1 = 'step1.csv'
output_file2 = 'step2.csv'
final_output = 'gcfinal.csv'
location = 7  # Location Name
field = 8  # Field Name
merged = 7  # Location and Field Merged
old_field = 8 # Cleanup old columnn
order = 0 # Remove unused column
round = 1 # Remove unused column
away = 2 # Away team column
home = 3 # Home team column
start = 5 # Start time
date = 4 # date column
end = 6 # end column
duration = 90
line2 = 1
year = '2023'
time_adjust = 12
t = time.strftime("%I:%M %p")


with open(input_file, 'r') as input_csv, open(output_file2, 'w', newline='') as step2_csv:

           reader = csv.reader(input_csv)
           writer = csv.writer(step2_csv)


           writer.writerow(['date', 'time', 'home', 'away', 'location', 'duration'])

           for row in reader:
            merged_text = f"{row[location]} - {row[field]}"
            row[merged] = merged_text
            row[round] = row[5]
            row[order] = row[date][:-2] + year
            row[date] = row[away]
            row[field] = duration
            del row[end]
            del row[5]
            del row[away]
            
            writer.writerow(row)  

       

with open('step2.csv', 'r') as step2_csv:
    csv_reader = csv.reader(step2_csv)


    
    rows = list(csv_reader)
          
del rows[1]

with open('step2.csv', 'w', newline='') as step2_csv:
    csv_writer = csv.writer(step2_csv)
    csv_writer.writerows(rows)   
           

     

    
        
            



        