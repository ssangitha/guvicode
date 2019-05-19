n=int(input())
l=list(map(int,input().split()))
a=[]
d=[]
for i in range(1):
	for j in range(i,n):
		a.append(sum(l[:j+1]))
b=a[::-1]
for i in range(n):
	d.append(str(a[i]+b[i]))
print(" ".join(d))
