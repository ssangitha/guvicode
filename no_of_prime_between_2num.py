a,b=map(int,input().split())
c=0
for i in range(a,b+1):
	for j in range(2,i+1):
		if i%j==0:
			break
	if j==i:
		c=c+1
print(c)
#...prime between 2 numbers....
