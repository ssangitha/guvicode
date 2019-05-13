n,k=map(int,input().split())
l=list(map(int,input().split()))
a=""
d=n-k
for i in range(d):
	a=a+str(l[i])+" "
print(a.strip())
