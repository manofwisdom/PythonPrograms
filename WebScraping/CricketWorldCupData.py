import requests
from BeautifulSoup import BeautifulSoup as BS

url ="https://en.wikipedia.org/wiki/List_of_ICC_Cricket_World_Cup_finals"
r = requests.get(url)
soup = BS(r.content)
rows = soup.findAll('table')[1].findAll('tr')
#print rows

year =""
winner =""
host =""
print "Year \t\t Winner   \t\t\t\t\t\t\t Host/s"
for row in rows[1:13]:
    year = row.findAll('th')[0].text
    winner = row.findAll('td')[0].text
    win = winner.replace('&#160;','')#[:-16]

    host = row.findAll('td')[4].text
    #print "year\t\t winner\t\t host"
    print year,"\t\t", win,"\t\t\t", host
