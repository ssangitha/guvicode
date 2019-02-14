n=int(input())
l=[]
a=""
for i in range(n):
	l1=list(map(int,input().split()))
	for j in l1:
		l.append(j)
l.sort()
for i in l:
	a=a+str(i)+" "
print(a.strip())
#.................sorting......
