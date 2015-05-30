'''
TO CREATE THE EXCEL SHEET FROM THE SCRAPED AND ORDERED DATA
'''

import xlwt as X
File = open("thedata.txt","r")
Book = X.Workbook()
Sheet = Book.add_sheet('PhoneArena Scraped',cell_overwrite_ok = True)
lines = File.readlines()
L = len(lines)
k=0
for i in range(L):
    line = lines[i]
    if ':::' in line:
        title = line.split(':::')[0]
        #Write to excel header into 1,k
        Sheet.write(1,k,title)
##        print "^^^^^^",title,"^^^^^^"
    if ';' in line:
        spec = line.split(';')[1]
        spec_id,spec_title = int(spec.split('_')[0]),spec.split('_')[1]
##        print spec_title
        #Write spec_title into spec_id,k
        Sheet.write(spec_id+2,k,spec_title)
    if '=' in line:
        k+=1
        print "****"*18

Book.save('TEST.xls')
