x,y=map(str,input().split())
i=0
j=0
z2=len(y)
z1=len(x)
if x==y:
	print("0")
else:
	a=x.index(y[0])
	if z2<z1:
		x,y=y,x
		z2,z1=z1,z2
	s=x[a:]
	z=len(s)
	while i<len(s) and j<len(s):
		if y[i]!=s[j]:
			a=a+1
			i=i+1
		else:
			i=i+1
			j=j+1
	d=abs(z2-z)
	print(a+d)
	
	#.......................
