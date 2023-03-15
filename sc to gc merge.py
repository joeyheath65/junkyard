import pandas as pd


df = pd.read_csv('step1.csv')


df['Date'] = pd.to_datetime(df['Date'], format='%m-%d-%Y')

# create a new column with the date formatted as 'Month Day, Year'
df['formatted_date'] = df['date'].dt.strftime('%B %d, %Y')