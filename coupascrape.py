import requests
from bs4 import BeautifulSoup

# Send an HTTP request to the website and store the response
url='https://amazon.coupahost.com/user/home'
req=requests.get(url)
print(req)
#content=req.text
#soup = BeautifulSoup(req.text, 'html.parser')
#print(soup)


    