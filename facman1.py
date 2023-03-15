import requests
from bs4 import BeautifulSoup

# Define the URLs for both websites
url1 = "https://sites.opstech.a2z.com/sites/SAT2/"
url2 = "https://facman.guardian.amazon.dev/dashboard/facilityPage#contentSectionId=26413&siteId=078564d9-9a03-481d-b1b7-4222f00d55e6"

# Make a request to both websites and retrieve their content
response1 = requests.get(url1)
content1 = response1.content

response2 = requests.get(url2)
content2 = response2.content

# Use BeautifulSoup to extract the content of the desired element
soup1 = BeautifulSoup(content1, 'html.parser')
soup2 = BeautifulSoup(content2, 'html.parser')

element1 = soup1.find("div", class_="d-flex user-alias-preview")
element2 = soup2.find("div", class_="container-fluid")

# Compare the content of both elements
if element1.text == element2.text:
    print("The content of both elements match.")
else:
    print("The content of both elements does not match.")
