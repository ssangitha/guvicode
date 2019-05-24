n=int(input())
l=list(map(int,input().split()))
if n==1:
	print(l[0])
else:
	for i in range(0,n):
		for j in range(i+1,n):
			t=l[i]^l[j]
	print(t)
