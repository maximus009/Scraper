from bs4 import BeautifulSoup
import requests
import xlwt as X

'''
THIS PROGRAM OPENS EACH OF THE 2466 LINKS AND SCRAPES FOR THE SPECIFICATIONS.

NEXT STEP IS TO ARRANGE THE DATA IN AN ORGANIZED FASHION AND CREATE A STRUCTURED DATABASE.
IN THE PROGRAM, THE 'Heads' DICTIONARY CONTAINS THE DATA.
THIS IS FURTHER TRANSPORTED TO "gsmarena_db.xls" TO STORE AS EXCEL SPREADSHEET.

'''
Book = X.Workbook()
Sheet = Book.add_sheet('GSMArena Database',cell_overwrite_ok=True)
f = open("phones_urls.txt","r")
phone_links = f.read().split(',')
L = len(phone_links)
for I in range(L):
    p = phone_links[I]
    url = 'http://www.gsmarena.com/'+p
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data)

    heads = soup.find_all("table")
    Heads = {}
    title = soup.find_all("div",{"id":"ttl","class":"brand"})
##    Manu = title[0].get_text().split(' ')[0].strip()
##    Make = title[0].get_text().split(' ')[1].strip()

    name = title[0].get_text().split(' ')
    Manu = name[0]
    Make = ' '.join(name[1:])
    for h in heads:
        j = h.find_all("th",{"scope":"row"})
        Heads[j[0].get_text()]=[]
        k = h.find_all("td",{"class":"ttl"})
        l = h.find_all("td",{"class":"nfo"})

        for i in range(len(k)):
            info ={}        
            info[k[i].get_text()]=l[i].get_text()
            Heads[j[0].get_text()].append(info)
    Heads[u'Product Info']=[{u'Brand':Manu},{u'Model':Make}]
    Keys = Heads.keys()
    for h in range(len(Keys)):
        Sheet.write(0,10*h,Keys[h])
    Vals = Heads.values()
    g=0
    r=0
    for V in Vals:
        for v in V:
            Sheet.write(1,r,v.keys()[0])
            Sheet.write(I+2,r,v.values()[0])
            r+=1
        g+=1
        r=10*g
    print I,"/",L
Book.save('gsmarena_db.xls')


