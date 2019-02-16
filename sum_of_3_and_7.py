n=int(input())
if n%3==0 or n%7==0:
	print("yes")
else:
	d=n//3
	c=n//7
	while d!=0:
		for i in range(1,c+1):
			a=(7*i)+(3*d)
			if a==n:
				print("yes")
				break
		if a==n:
			break
		else:
			d=d-1
	if d==0:
		print("no")
