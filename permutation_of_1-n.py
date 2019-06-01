n=int(input())
l=list(map(int,input().split()))
ind=[]
c=0
for j in range(1,n+1):
	ind.append(j)
for i in range(n):
	if l[i]!=ind[i]:
		print("no")
		break
	else:
		c=c+1
if c==n:
	print("yes")
