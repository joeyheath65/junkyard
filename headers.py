import csv
import pandas as pd
import datetime

df = pd.read_csv('input.csv')
df = df.rename(columns={'Date': 'date'})


print(df)



