def fact(a):
	c=1
	for i in range(1,a+1):
		c=c*i
	return(c)
n,r=map(int,input().split())
b=fact(n)
g=fact(n-r)
print(b//g)
