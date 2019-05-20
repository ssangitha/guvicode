n,m=map(int,input().split())
l=list(map(str,input().split()))
a=[]
b=l[:n]
c=l[n:]
for i in c:
	if i in b:
		a.append(i)
		b.remove(i)
a.sort()
print(" ".join(a))
