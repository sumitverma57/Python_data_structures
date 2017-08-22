import sys
import os

lst=os.listdir(sys.argv[1])
size=[]
for i in range(len(lst)):
	size.append(os.stat(lst[i]).st_size)
m=max(size)
print m
j=size.index(m)
print os.path.realpath(lst[j])
