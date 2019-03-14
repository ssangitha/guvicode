s=input()
a=s[::-1]
if a==s:
	print(s)
else:
	l=[]
	for i in range(0,len(s)-1):
		for j in range(len(s),i+1,-1):
			b=s[i:j]
			x=b[::-1]
			if b==x:
				l.append(b)
	c=len(l[0])
	z=l[0]
	for i in l:
		if c<len(i):
			c=len(i)
			z=i
	print(z)
	
	
		
