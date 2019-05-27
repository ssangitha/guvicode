n=int(input())
l=list(map(int,input().split()))
x=[]
c=1
a=l
for i in range(n):
	b=a[i]
	a[i]=1
	for j in a:
		c=c*j
	x.append(str(c))
	c=1
	a[i]=b
print(" ".join(x))
