n,m=map(int,input().split())
l=list(map(int,input().split()))
a=list(map(int,input().split()))
for i in a:
	if i in l:
		l.remove(i)
		c=0
	else:
		c=1
		break
if c==0:
	print("YES")
else:
	print("NO")
