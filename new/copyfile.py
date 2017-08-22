import sys
ls1=open(sys.argv[1],'r')
ls2=open(sys.argv[2],'w')
m=ls1.read()
ls2.write(m)
