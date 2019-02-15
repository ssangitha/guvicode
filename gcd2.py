n,m=map(int,input().split())
if n%m==0 or m%n==0:
	print(min(n,m))
else:
	g=min(n,m)
	for i in range(1,g+1):
		if n%i==0 and m%i==0:
			g=i
	print(g)
 #..........gcd.........
