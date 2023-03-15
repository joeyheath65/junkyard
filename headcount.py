import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize
import csv


gearing = requests.get('https://w.amazon.com/bin/view/FC_IT_Finance/FieldHeadcountGuidelines/', verify=False)

df_list = pd.read_html(gearing)
#df = df_list[-1]
#print(df)
#df.to_csv('headcount.csv')
