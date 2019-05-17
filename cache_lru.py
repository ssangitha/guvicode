n,k=map(int,input().split())
l=list(map(int,input().split()))
s=[]
for i in range(n-k,n):
	s.append(str(l[i]))
print(" ".join(s))
