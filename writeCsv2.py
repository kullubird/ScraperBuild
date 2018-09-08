import csv

f = open('names.csv', 'a')
x=[33,3,3,3,3,3,3]

with f:
    
    fnames = ['playerInfo','min1','min2','min3','min4','min5']
    writer = csv.DictWriter(f, fieldnames=fnames,lineterminator = '\n')    

    #writer.writeheader()
    writer.writerow({'playerInfo':'1 gold','min1':'500','min2':'500','min3':'500','min4':'500','min5':'500'})

    