n=int(input())
l=list(map(int,input().split()))
m=1
p=[]
for i in range(n-1):
	for j in range(i+1,n):
		c=l[i:j+1]
		for k in c:
			m=m*k
		p.append(m)
		m=1
p.sort()
print(p[-1])
