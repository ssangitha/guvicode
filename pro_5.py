n,a,b=map(int,input().split())
if n %2!=0:
	print("NO")
else:
	x=n//2
	s=0
	i=1
	j=1
	for i in range(1,x):
		for j in range(1,x):
			s=(a*i)+(b*j)
			if s==x:
				break
		if s==x:
			break
	if s==x:
		print("YES")
	else:
		print("NO")
#.....................
