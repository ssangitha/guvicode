n=int(input())
a=[]
c=0
for i in range(2,n):
	for j in range(2,i+1):
		if i%j==0:
			break
	if j==i:
		a.append(i)
for i in range(len(a)):
	for j in range(len(a)):
		if a[i]+a[j]==n:
			print(str(a[i])+" "+str(a[j]))
			c=1
			break
	if c==1:
		break
	
