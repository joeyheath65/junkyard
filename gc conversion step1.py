import csv
import os
import pandas as pd
from datetime import datetime



input_file = 'input.csv'
output_file = 'gcschedule.csv'
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




with open(input_file, 'r') as input_csv, open(output_file, 'w', newline='') as gcschedule_csv:

        reader = csv.reader(input_csv)
        writer = csv.writer(gcschedule_csv)    
        
        for row in reader:
            starttime = int(start)
            merged_text = f"{row[location]} - {row[field]}"
            row[merged] = merged_text
            row[round] = row[start]
            row[order] = row[date]
            row[date] = row[away]
            row[field] = duration
            del row[end]
            del row[start]
            del row[away]

        writer.writerow(row)


