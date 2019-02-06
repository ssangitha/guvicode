n=int(input())
l=[]
x=""
for i in range(n):
	c=input()
	l.append(c)
a=min(l)
d=len(a)
for i in range(1,d+1):
	s=a[0:i]
	if all(j[0:i]==s for j in l):
		x=s
print(x)
#...longest prefix....
