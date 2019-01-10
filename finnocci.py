# fibbcc.......
n=int(input())
s=""
a=1
b=1
s=str(a)+" "+str(b)
for i in range(2,n):
	c=a+b
	s=s+" "+str(c)
	a=b
	b=c
print(s.strip())
