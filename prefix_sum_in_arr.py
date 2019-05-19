n=int(input())
l=list(map(int,input().split()))
a=[]
for i in range(1):
	for j in range(i,n):
		a.append(str(sum(l[:j+1])))
print(" ".join(a))
	
