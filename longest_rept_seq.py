n=int(input())
l=list(map(int,input().split()))
c=1
m=c
f=1
for i in range(n-1):
	if l[i]==l[i+1]:
		c=c+1
		f=c
	elif c>m:
		m=c
		f=c
		c=1
print(f)
