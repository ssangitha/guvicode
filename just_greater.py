n,k=map(int,input().split())
l=list(map(int,input().split()))
a=[]
l.sort(reverse=True)
for i in l:
	if i>k:
		a.append(i)
print(a[-1])
