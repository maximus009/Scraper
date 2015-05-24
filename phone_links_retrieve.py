'''
THIS PROGRAM OPENS THE GSMARENA PAGE WHICH ENLISTS ALL OF THE MAKERS OF MOBILE PHONES AND DEVICES.

THE SCRAPER FIRST SAVES ALL OF THE INDIVIDUAL LINKS. (101 IN NUMBER)

THE SCRAPER THEN STORES THESE URLs IN A TEXT FILE "PHONE_URL.TXT".

'''


from bs4 import BeautifulSoup
import requests

url = 'http://www.gsmarena.com/makers.php3'
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data)

B = soup.find_all("table")
manu_links = []
links = B[0].find_all('a')
for l in links[::2]:
    manu_links.append(l['href'])

I = len(manu_links)

for i in range(I):
    ml = manu_links[i]
    url = 'http://www.gsmarena.com/'+ml
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data)
    phonetabs = soup.find_all("div",{"class":"makers"})
    phone_links=[]
    for p in phonetabs:
        link = p.find_all('a')
        for l in link:
            phone_links.append(l['href'])
    f = open("phones_urls.txt","a")
    for p in phone_links:
        f.write(p+",")
    f.close()
