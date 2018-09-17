import csv

from pathlib import Path


matchId=6969
tempFilePath="Scraped Data/"+str(matchId)+".csv"

tf=Path(tempFilePath)

if tf.is_file():
	print("doh")

f = open(tempFilePath, 'a')
x=[33,3,3,3,3,3,3]

fnames = ['playerInfo','min1','min2','min3','min4','min5']
writer = csv.DictWriter(f, fieldnames=fnames,lineterminator = '\n')    
writer.writeheader()
#writer.writeheader()
writer.writerow({'playerInfo':'1 gold','min1':'500'
	,'min2':'500','min3':'500','min4':'500'})

    