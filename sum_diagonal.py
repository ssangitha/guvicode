n=int(input())
l=[]
c=0
for i in range(n):
	x=list(map(int,input().split()))
	l.append(x)
for i in range(n):
	for j in range(n):
		if i==j:
			c=c+l[i][j]
print(c)
