n=int(input())
l=list(map(int,input().split()))
z=[]
for i in range(n):
	if i%2==0 and l[i]%2==1:
		z.append(str(l[i]))
	elif i%2==1 and l[i]%2==0:
		z.append(str(l[i]))
print(" ".join(z))
