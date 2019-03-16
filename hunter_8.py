n=int(input())
l=list(map(int,input().split()))
for i in range(0,n-2):
	for j in range(i+1,n-1):
		for k in range(j+1,n):
			if l[i]+l[j]==l[k]:
				print(str(l[i])+" "+str(l[j])+" "+str(l[k]))
