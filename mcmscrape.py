
import requests
from bs4 import BeautifulSoup as bs
  
URL = 'https://mcm.amazon.com/search?scheduled_start[predicate]=Between&scheduled_start[values][]=Today&'
  
req = requests.get(URL)
soup = bs(req.text, 'html.parser')
  
titles = soup.find('div',attrs = {'class','head'})
  
print(titles.text)