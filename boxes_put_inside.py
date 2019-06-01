n=int(input())
l=list(map(int,input().split()))
c=1
for i in range(n-1):
	if l[i]>l[i+1] or l[i]==l[i+1]:
		c=c+1
print(c)
