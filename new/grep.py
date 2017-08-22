import sys
f=open(sys.argv[1])
lst=f.readlines()
m=len(lst)
patt=sys.argv[2]
for i in range(m):
	if(patt in lst[i]):
		print(lst[i])

			