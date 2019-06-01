a,b=input().split()
if len(a)==len(b):
	print(a+b)
elif len(a)>len(b):
	c=a[:len(b)]+b
	print(c)
else:
	c=a+b[:len(a)]
	print(c)
