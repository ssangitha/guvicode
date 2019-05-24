n=int(input())
l=list(map(int,input().split()))
a=[]
if n==1:
	print(l[0])
else:
	for i in range(n-1):
		a.append(l[i]|l[i+1])
	print(max(a))
