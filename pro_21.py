n=int(input())
l=list(map(int,input().split()))
for i in range(1,len(l)+1):
	if i!=len(l):
		a=l[:i]
		b=l[i:]
		c=sum(a)
		d=sum(b)
		if c//len(a)==d//len(b):
			print("yes")
			break
	else:
		print("no")
		break
