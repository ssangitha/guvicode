n,a,b=map(int,input().split())
x=n//2
s=0
i=1
j=1
while s<x:
	s=(a*i)+(b*j)
	if s==x:
		print("YES")
		break
	else:
		i=i+1
		j=j+1
if s>x:
	print("NO")
#.....................
