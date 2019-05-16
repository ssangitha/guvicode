n=int(input())
l=list(map(int,input().split()))
d=[]
for i in range(n-1):
	for j in range(i+1,n):
		d.append(abs(l[i]-l[j]))
d.sort()
while 0 in d: d.remove(0)
print(d[0])
