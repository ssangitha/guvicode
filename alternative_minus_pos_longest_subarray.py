n=int(input())
l=list(map(int,input().split()))
b=[]
c=1
for i in range(n):
	a=l[i:]
	m=len(a)
	for j in range(m-1):
		if a[j]>0 and a[j+1]<0:
			c=c+1
		elif a[j]<0 and a[j+1]>0:
			c=c+1
		else:
			break
	b.append(str(c))
	c=1
print(" ".join(b))
