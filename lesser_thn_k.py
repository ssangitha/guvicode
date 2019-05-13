n,k=map(int,input().split())
l=list(map(int,input().split()))
p=[]
a=""
for i in l:
	if i<k:
		p.append(i)
p.sort()
for i in p:
	a=a+str(i)+" "
print(a.strip())
