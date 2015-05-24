'''
IMAGE DOWNLOADS

DOWNLOADS IMAGES FROM EACH OF THE SCRAPED PAGES OF EACH AND EVERY PHONE IN GSMARENA
AND SAVES THE IMAGES WITH THEIR FILENAME, ALSO GROUPING SIMILAR PHONES IN
THE SAME FOLDER.

I CERTIFY THIS AS A COOL PROGRAM FOR EVERYONE TO USE.

'''
import os
import urllib
import urllib2
import urlparse
from urllib import urlretrieve
from bs4 import BeautifulSoup as bs

f = open("phones_urls.txt","r")
links = f.read().split(',')
L = len(links)

for I in range(400,L):
    try:
        url = 'http://www.gsmarena.com/'+links[I]
        newrl = url[:-8]+'pictures'+url[-9::]

        html = urllib2.urlopen(newrl)

        soup = bs(html)
        imgs= soup.find_all("p",{"align":"center"})
        title = soup.find_all("div",{"class":"brand","id":"ttl"})
        name = title[0].get_text().strip()
        name = '_'.join(name.split(' '))
        name=str(I)+name
    ##    if name.find(';')>0:
    ##        name.replace(';','')
    ##    print name    
        img1 = []
        for i in imgs:
            j = i.find({"img":"src"})
            img1.append(j['src'])

        os.system("mkdir "+name)


        for img in img1:
            img_url = urlparse.urljoin(url, img)
            file_name = img.split('/')[-1]
            urlretrieve(img_url, name+"\\"+file_name)
        print I,
    except IOError:
        continue
