n=int(input())
l=list(map(int,input().split()))
s=[]
c=0
for i in range(0,n-2):
	for j in range(i,n,2):
		c=c+l[j]
	s.append(c)
	c=0
s.sort()
print(s[-1])
	
