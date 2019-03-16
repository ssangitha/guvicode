n=int(input())
l=list(map(int,input().split()))
x=0
for i in range(n):
	c=l.count(l[i])
	if c!=1:
		print(l[i])
		x=1
		break
if x==0:
	print("unique")
