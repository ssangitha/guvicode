n,m=map(int,input().split())
mi=min(n,m)
for i in range(1,mi+1):
	if n%i==0 and m%i==0:
		g=i
print(g)
