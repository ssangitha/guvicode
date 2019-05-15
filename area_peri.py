a,b=map(int,input().split())
c=1
for i in range(1,a+1):
	for j in range(1,a+1):
		if i*j==b and 2*(i+j)==a:
			c=0
			break
if c==0:
	print("yes")
else:
	print("no")
