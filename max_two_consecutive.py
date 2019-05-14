n=int(input())
l=list(map(int,input().split()))
p=[]
s=""
for i in range(n-1):
	c=max(l[i],l[i+1])
	p.append(c)
for i in p:
	s=s+str(i)+" "
print(s.strip())
