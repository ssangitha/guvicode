n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(n-1):
	a.append(l[i]+l[i+1])
print(sum(a))
