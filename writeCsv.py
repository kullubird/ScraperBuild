import numpy as np 
import csv
import pandas as pd

col1_array=[1,2,3,4,5,6]
col2_array=[7,7,7,7,7,7]

# col3_array=[5","2","3"]

# str1 = ','.join(col1_array)
# str2 = ','.join(col2_array)

# arrayStr1=[]
# arrayStr2=[]
# for i in range(5):
# 	arrayStr1.append(str1)
# 	arrayStr2.append(str2)


#a = np.array(col1_array)
#df1 = pd.DataFrame({"a": [a]})

#b = np.array(col2_array)
#df2 = pd.DataFrame({"a": [a]})

a=str(col1_array)

with open('data.csv', 'a') as file:

	np.savetxt(file, (a,a),fmt="%s")
	