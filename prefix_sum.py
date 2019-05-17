n=int(input())
l=list(map(int,input().split()))
s=[]
for i in range(n):
	if l[i]%2==0:
		c=l[:i+1]
		s.append(str(sum(c)))
	else:
		s.append(str(l[i]))
print(" ".join(s))
