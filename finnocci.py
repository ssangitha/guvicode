# fibbcc.......
n=int(input())
a=1
b=1
print(a,b,end=" ")
for i in range(2,n):
	c=a+b
	print(c,end=" ")
	a=b
	b=c
