n,k=map(int,input().split())
z=[]
c=""
for i in range(n):
	l=list(map(int,input().split()))
	z.append(l)
for i in range(k):
	if all(z[0][i] in z[k] for k in range(1,n)):
		c=c+str(z[0][i])+" "
print(c.strip())
