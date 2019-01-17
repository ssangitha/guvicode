n=int(input())
if n==2:
	print("no")
else:
	
	for i in range(2,(n//2)+1):
		if n%i==0:
			print("yes")
			break
	if i==n//2:
		print("no")
