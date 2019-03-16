n=int(input())
l=list(map(int,input().split()))
c=l.count(0)
z=[]
for i in l:
	if i!=0:
		z.append(str(i))
for i in range(c):
	z.append(str(0))
print(" ".join(z))
