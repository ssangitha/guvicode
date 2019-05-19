n=int(input())
l=list(map(int,input().split()))
a=[]
b=""
for i in l:
	a.append([str(l.index(i)+1),i])
a.sort(key=lambda x:x[1])
for i in range(n):
	b=b+a[i][0]+" "
print(b.strip())
