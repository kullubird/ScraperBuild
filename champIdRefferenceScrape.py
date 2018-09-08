import csv
reader = csv.reader(open('Scraped Data\Champions.csv', 'r'))
d={}
for row in reader:
	k, v = row
	d[k] = v
	print(d[k])

champId=21
#if str(champId) in d:
print(d[str(champId)])