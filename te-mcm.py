import requests
import sys
import csv
from bs4 import BeautifulSoup

data = open('https://mcm.amazon.com/search?requester[predicate]=In&requester[values][]=bowmanta&scheduled_start[predicate]=GreaterThanEqual&scheduled_start[values][]=01%2F01%2F2022%2000%3A00&').read
soup = BeautifulSoup(data,'html.parser')
result = soup.find('top-padding')
mcmtech = result.h4.a.text
content = result.find_('div' ,class_='search_stats.top-padding-2-em')

print(content)
print(mcmtech)

for div in content:
    print(div.text)

    