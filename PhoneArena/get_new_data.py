'''
TO GET THE COLUMNS
'''

import glob
files = glob.glob("*_FullDetails_*.txt")
L = len(files)
F = open("DATA.txt","a")
cols = {}
cols['Manufacturer']=[]
cols['Model']=[]
for I in range(L):
    id = files[I].split('_')[0]
    Name = files[I].split('s_')[1]
    Manu = Name.split('-')[0]
    Make = ' '.join(Name.split('-')[1:]).split('_id')[0]

    model = open(files[I],"r")
    specs = model.readlines()
    cols['Manufacturer'].append(id+"_"+Make)
    cols['Model'].append(id+'_'+Make)
    for s in specs:
        if s.find(':::')!=-1:
            col = s.split(':::')
            if col[0] not in cols:
                cols[col[0]]=[id+'_'+col[1]]
            else:
                cols[col[0]].append(id+'_'+col[1])

for C in cols.keys():
    F.write(C+":::")
    for e in cols[C]:
        F.write(e+';')
    F.write('\n')
        
