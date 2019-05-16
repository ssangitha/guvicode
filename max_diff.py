n=int(input())
l=list(map(int,input().split()))
d=[]
for i in range(n-1):
	for j in range(i+1,n):
		d.append(abs(l[i]-l[j]))
d.sort(reverse=True)
print(d[0])
