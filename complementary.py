a=input()
b=input()
c=a+b
x=1
if len(c)!=26:
	print("non-complementary")
	x=0
else:
	for i in c:
		if c.count(i)!=1:
			print("non-complementary")
			x=0
			break
if x==1:
	print("complementary")
