'''
To store the links of all th relevant manufacturers from Phone Arena

'''

import requests
from bs4 import BeautifulSoup as bs

url = 'http://www.phonearena.com/phones/manufacturers'
dr= requests.get(url)
data = dr.text
soup = bs(data)
f = open("links.txt","w")
phones = soup.find_all("div",{"class":"s_hover"})
for p in phones:
    print p.find_all("a")[0].attrs['href'].split("/")[-1],
    print " Save? "
    c = raw_input()
    if c == 'y':
        f.write(p.find_all("a")[0].attrs['href'])
    if c=="":
        continue
f.close()
