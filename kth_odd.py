n,k=map(int,input().split())
l=list(map(int,input().split()))
a=0
for i in l:
	if i%2==1:
		a=a+1
		if a==k:
			break
print(i)
#......odd....
