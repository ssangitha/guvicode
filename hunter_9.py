n=int(input())
l=list(map(int,input().split()))
m=max(l)
for i in range(0,n-1):
	for j in range(i+1,n):
		c=abs(l[i]+l[j])
		if c<m:
			m=c
			a,b=str(l[i]),str(l[j])
print(a+" "+b)
