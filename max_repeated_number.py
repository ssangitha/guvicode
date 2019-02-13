n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
	d=l.count(i)
	if d>c:
		c=d
		max=i
print(max)
#....max repeated number....
