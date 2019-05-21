n,k=map(int,input().split())
l=list(map(int,input().split()))
a=[]
if k in l:
	print(k)
else:
	l.sort()
	for i in l:
		if i<k:
			a.append(i)
	print(a[-1])
