s=input()
c=s
a=1
while(" " in c):
	c=c.replace(" ","")
n=len(c)
if n==2:
	print("yes")
else:
	for i in range(2,n):
		if n%i==0:
			a=0
			break
	if i==n-1 and a==1:
		print("yes")
	else:
		print("no")
