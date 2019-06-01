n,k=input().split()
k=int(k)
c=0
for i in range(k+1):
	if str(i) in n:
		c=1
	else:
		c=0
		break
if c==1:
	print("yes")
else:
	print("no")
