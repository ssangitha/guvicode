a,b=input().split()
if len(a)>len(b):
	a=a
	b=b
else:
	a,b=b,a
if all(i in b for i in a):
	print("true")
else:
	print("false")
