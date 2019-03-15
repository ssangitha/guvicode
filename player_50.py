n=int(input())
if n==2:
	print("no")
else:
	for i in range(2,n):
		if n%i==0:
			x=0
			break
		else:
			x=1
	if x==0:
		print("yes")
	else:
		print("no")
