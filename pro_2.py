n,k=map(int,input().split())
n=str(n)
d=len(n)-k
l=[]
if k==0:
	print(n)
else:
	for i in range(0,(len(n)-d)+1):
		a=int(n[i:i+d])
		l.append(a)
	print(min(l))
