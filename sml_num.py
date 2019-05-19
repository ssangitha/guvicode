n=int(input())
l=list(map(int,input().split()))
b=[str(l[0])]
for i in range(1,len(l)):
	c=l[:i+1]
	b.append(str(min(c)))
print(" ".join(b))	
