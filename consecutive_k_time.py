n,k=map(int,input().split())
a=input()
c=1
for i in range(n-1):
	b=input()
	if a==b:
		x=0
		c=c+1
		if c==k:
			break
	else:
		a=b
if c==k:
	print("yes")
else:
	print("no")
	
