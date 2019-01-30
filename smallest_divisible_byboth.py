n,m=map(int,input().split())
if n%m==0 or m%n==0:
	print(max(n,m))
elif n%10==0 and m%10==0:
	n=str(n)
	m=str(m)
	a=max(len(n),len(m))
	s=n[0]
	x=m[0]
	q=int(s)*int(m)
	print(q+(0*(a-1)))
else:
	print(m*n)

#....smallest divisible by both number...
