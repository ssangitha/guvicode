n=int(input())
l=list(map(int,input().split()))
min=l.count(l[0])
a=0
for i in range(1,n):
	m=l.count(l[i])
	if min>m:
		min=m
		a=i
print(l[a])
