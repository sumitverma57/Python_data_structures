import sys

f= open(sys.argv[1])
lst=f.readlines()
m=len(lst)
sum1=0
for i in range(m):
	sum1+=int(lst[i])

print(sum1) 

