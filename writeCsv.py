import numpy as np 
import csv
import pandas as pd

# col1_array=["1","2","3"]
# col2_array=["4","2","3"]

# col3_array=["5","2","3"]

# str1 = ','.join(col1_array)
# str2 = ','.join(col2_array)

# arrayStr1=[]
# arrayStr2=[]
# for i in range(5):
# 	arrayStr1.append(str1)
# 	arrayStr2.append(str2)


a = np.array([5, 6, 7, 8])
df1 = pd.DataFrame({"a": [a]})

b = np.array([8, 6, 7, 8])
df2 = pd.DataFrame({"a": [a]})

with open('D:\Studies\Research\ScraperBuild\data.csv', 'a') as file:

	np.savetxt(file, (a,b),fmt="%s")
	