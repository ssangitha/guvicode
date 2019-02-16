n,k=map(int,input().split())
n=str(n)
d=len(n)-k
j=1
m=min(n)
a=m
if k==0:
	print(n)
else:
	while(j<d):
		i=n.index(m)
		x=n[i+1:]
		m=min(x)
		a=a+m
		j=j+1
	print(a)
