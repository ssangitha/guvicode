n,k=map(int,input().split())
input()
a=""
l=list(map(int,input().split()))
k1=list(map(int,input().split()))
for i in k1:
	l.append(i)
	c=max(l)
	a=a+str(c)+" "
print(a.strip())
