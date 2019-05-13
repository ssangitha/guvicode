n,k=map(int,input().split())
l=list(map(int,input().split()))
p=[]
a=""
for i in l:
	if l.count(i)==k and i not in p:
		p.append(i)
for i in p:
	a=a+str(i)+" "
print(a.strip())
