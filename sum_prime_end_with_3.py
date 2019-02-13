n=int(input())
l=[]
for i in range(2,n):
	for j in range(2,i+1):
		if i%j==0:
			break
	if i==j and i%10==3:
		l.append(i)
print(sum(l))
