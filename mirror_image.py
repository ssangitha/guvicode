n=int(input())
c=0
l=list(map(int,input().split()))
m=list(map(int,input().split()))
for i in range(n):
	if l[i]!=m[(n-1)-i]:
		print("no")
	else:
		c=c+1
if c==n:
	print("yes")
