a,b=map(int,input().split())
l=[]
r=0
for i in range(a,b+1):
	c=bin(i)[2:]
	d=c.count("1")
	l.append(d)
for j in l:
	if j!=1:
		for k in range(2,j+1):
			if j%k==0:
				break
		if j==k:
			r=r+1
print(r)
