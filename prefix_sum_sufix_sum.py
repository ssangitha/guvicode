n=int(input())
l=list(map(int,input().split()))
x=1
for i in range(1,n-1):
	a=l[:i]
	b=l[i+1:]
	if sum(a)==sum(b):
		x=0
		print("yes")
		break
if x==1:
	print("no")
