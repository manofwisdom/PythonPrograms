import requests
import re
from BeautifulSoup import BeautifulSoup

url ="https://in.finance.yahoo.com/"

r = requests.get(url)

soup = BeautifulSoup(r.content)

sensex = soup.findAll('span', {"id":"yfs_l84_^bsesn"})[0].text
nifty = soup.findAll('span', {"id":"yfs_l84_^nsei"})[0].text
print "sensex: ",sensex
print "nifty: ",nifty
