n,k=map(int,input().split())
li=list(map(int,input().split()))
for x in range(n):
	if li[x]==k:
		print("yes")
		break
if x==n-1:
	print("no")
#........yes or no......
