
import requests
from BeautifulSoup import BeautifulSoup as BS

url = "https://en.wikipedia.org/wiki/List_of_missions_to_the_Moon"
r = requests.get(url)
soup =BS(r.content)

tables = soup.findAll('table')[0].findAll('tr')
print len(tables)
#print tables

spacecraft =[]
launch_date = []
mission = []
outcome = []

p = ""
q = ""
r = ""
s = ""

for row in tables[1:126]:
    p = row.findAll('td')[0].text
    q = row.findAll('td')[1].text
    r = row.findAll('td')[4].text
    s = row.findAll('td')[5].text
    #print p,"\t\t", r,"\t\t",s
    spacecraft.append(p)
    launch_date.append(q)
    mission.append(r)
    outcome.append(s)
