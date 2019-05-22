l,r,n=map(int,input().split())
c=0
n=str(n)
for i in range(l,r+1):
	a=str(i)
	if n in a:
		c+=1
print(c)
