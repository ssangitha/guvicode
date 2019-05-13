n,k=map(int,input().split())
l=list(map(int,input().split()))
a=1
for i in range(0,n-1):
	for j in range(i+1,n):
		if l[i]+l[j]==k:
			a=0
			break
	if a==0:
		break
if a==0:
	print("yes")
else:
	print("no")
