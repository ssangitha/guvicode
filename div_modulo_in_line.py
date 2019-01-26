s=input()
a=""
b=""
if "/" in s:
	i=s.index("/")
	a=s[0:i-1]
	b=s[i+2:]
	print(int(a)//int(b))
elif "%" in s:
	i=s.index("%")
	a=s[0:i-1]
	b=s[i+2:]
	print(int(a)%int(b))
	
