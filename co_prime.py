x,y=input().split()
n=len(x)
m=len(y)
g=min(n,m)
for i in range(1,g+1):
	if n%i==0 and m%i==0:
		g=i
if g==1:
	print("yes")
else:
	print("no")
