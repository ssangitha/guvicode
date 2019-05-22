n,k=map(int,input().split())
a=[]
for i in range(n,k+1):
	if i%2==1:
		a.append(i)
print(sum(a))
#
