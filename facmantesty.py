import requests
from bs4 import BeautifulSoup

def compare_fields(url1, url2, field_tag, field_class):
    # retrieve the contents of the first URL
    response1 = requests.get(url1)
    soup1 = BeautifulSoup(response1.text, 'html.parser')
    field1 = soup1.find(field_tag, class_=field_class).text

    # retrieve the contents of the second URL
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.text, 'html.parser')
    field2 = soup2.find(field_tag, class_=field_class).text

    # compare the contents of the two fields
    return field1 == field2

# example usage
url1 = "https://facman.guardian.amazon.dev/dashboard/facilityPage#siteId=078564d9-9a03-481d-b1b7-4222f00d55e6"
url2 = "https://sites.opstech.a2z.com/sites/SAT2"
field_tag = "p"
field_class = "content"

are_fields_equal = compare_fields(url1, url2, field_tag, field_class)
if are_fields_equal:
    print("The fields are the same")
else:
    print("The fields are different")
