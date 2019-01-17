n,m=map(int,input().split())
c=m*n
for i in range(100):
	if(i*i==c):
		print("yes")
		break
if(i==99):
	print("no")
