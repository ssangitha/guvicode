n=int(input())
p=[]
a=""
l=list(map(int,input().split()))
m=list(map(int,input().split()))
for i in l:
	if i in m and i not in p:
		p.append(i)
for i in p:
	a=a+str(i)+" "
print(a.strip())
