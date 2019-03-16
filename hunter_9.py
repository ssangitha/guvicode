n=int(input())
l=list(map(int,input().split()))
for i in range(0,n-1):
	for j in range(i+1,n):
		if l[i]+l[j]==0:
			print(str(l[i])+" "+str(l[j]))
			break
