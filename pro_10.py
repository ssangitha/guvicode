n=int(input())
l=list(map(int,input().split()))
z=[0]
for i in range(1,len(l)):
	for j in range(i):
		if l[j]<l[i]:
			z.append(l[j])
print(sum(z))
#detective problem
