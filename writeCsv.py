import numpy as np 
import csv

col1_array=["1","2","3"]
col2_array=["1","2","3"]

col3_array=["1","2","3"]

with open('D:\Studies\Research\ScraperBuild\data.csv', 'a') as file:

	np.savetxt(file, (col1_array, col2_array, col3_array), delimiter=',',fmt="%s")
#with open(r'data.csv', 'a') as f:
#    writer = csv.writer(f)
#   writer.writerow(col1_array)