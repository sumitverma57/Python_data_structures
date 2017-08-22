import sys
import os
try:
	print(os.listdir(sys.argv[1]))

except:
 	h=os.getcwd()
	print(os.listdir(h))
