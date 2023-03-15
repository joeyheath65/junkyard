str = 'joseheat@amazon.com, page-joseheat@amazon.com'

page = urllib.request.urlopen("http://website/category")
## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str) 
    ## ['alice@google.com', 'bob@abc.com']    
for email in emails:
    # do something with each found email string
    print email

import BeautifulSoup
import re
import urllib

data = urllib.urlopen('http://listadecasamento.fastshop.com.br/ListaCasamento/ListaCasamentoBusca.aspx?Data=2013-06-07').read()
soup = BeautifulSoup.BeautifulSoup(data)
element = soup.find('span', attrs={'class': re.compile(r".*\btxt_resultad_busca_casamento\b.*")})
print element.text