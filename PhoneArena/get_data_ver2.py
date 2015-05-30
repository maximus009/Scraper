'''
To store the links of all th relevant Indian manufacturers from Phone Arena

'''

import requests
from bs4 import BeautifulSoup as bs

Url = 'http://www.phonearena.com'
Links = open("phones_urls.txt","r").read().split("\n")
L = len(Links)
for I in range(559,L):
    p = Links[I]
    Name = p.split('/')[-1]
    url = Url + p + '/fullspecs'
    dr= requests.get(url)
    data = dr.text
    soup = bs(data)
    T =[]
    V = []
    lss = soup.find_all("li",{"class":"s_lv_1"})
    for l in lss:
        L =  l.get_text()
##        print "%%"*29
        L=L.split(':')
##        print len(L)
        if len(L) == 1:
            continue
        if len(L)==2:
            T.append(L[0])
            V.append(L[1].strip())
        if len(L)>2:
            T.append(L[0])
            V.append(''.join(L[1:]).strip())
    g = open(str(I)+"_FullDetails_"+Name+".txt","w")
    for i in range(len(V)):
        try:
            g.write(T[i]+":::"+V[i]+"\n")
        except UnicodeEncodeError:
            pass
    g.close()
    print I,
