x,y=map(str,input().split())
i=1
j=1
z2=len(y)
if x==y:
	print("0")
else:
	a=x.index(y[0])
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
