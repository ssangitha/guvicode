n=input()
c=1
if n==n[::-1]:
	print("yes")
else:
	x=n.strip("0")
	if x==x[::-1]:
		c=0
	if c==0:
		print("yes")
	else:
		print("no")
