m,n=map(int,input().split())
p=m*n
d=0
c=bin(p)[2:]
for i in range(len(c)):
	if c[i]=="1":
		d=d+1
	if d==2:
		print(i+1)
		break
