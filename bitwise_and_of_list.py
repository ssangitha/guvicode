n=int(input())
l=list(map(int,input().split()))
if n==1:
	print(l[0])
else:
	s=l[0]
	for i in range(0,n):
		s=s&l[i]
	print(s)
