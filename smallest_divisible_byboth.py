n,m=map(int,input().split())
if n%m==0 or m%n==0:
	print(max(n,m))
else:
	g=max(n,m)
	while(True):
		if g%n==0 and g%m==0:
			print(g)
			break
		g=g+1
#....smallest divisible by both number...
