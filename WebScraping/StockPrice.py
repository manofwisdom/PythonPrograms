import requests
from BeautifulSoup import BeautifulSoup
companies =['GOOGL.BA', "AAPL", 'YHOO']
i=0
while i<len(companies):
    url ="https://in.finance.yahoo.com/q?s="+companies[i]
    r =requests.get(url)
    soup =BeautifulSoup(r.content)
    price =soup.findAll('span', {"id":"yfs_l84_"+companies[i]})[1].text
    print price
    i+=1
