from itertools import combinations
n,k,t=map(int,input().split())
l=list(map(int,input().split()))
c=0
x= list(combinations(l,k))
for i in range(len(x)):
	if sum(x[i])==t:
		c=1
		print("YES")
		break
if c==0:
	print("NO")
