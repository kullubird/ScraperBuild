# test to catch an exception

import time

flag=1
i=0
try:
	while flag!=0:
		time.sleep(1)
		i=i+1
except KeyboardInterrupt:
	print(i)



