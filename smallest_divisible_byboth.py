n,m=map(int,input().split())
if n%m==0 or m%n==0:
	print(max(n,m))
else:
	print(m*n)
#....smallest divisible by both number...
