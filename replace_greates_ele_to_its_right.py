n=int(input())
l=list(map(int,input().split()))
m=[]
s=" "
for i in range(n-1):
	c=l[i+1:]
	m.append(str(max(c)))
m.append("0")
print(s.join(m))
