c=0
n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
	d=i
	while(d!=0):
		d=d&(d-1)
		c=c+1
	l1.append(c)
	c=0
for i in range(0,len(l)-1):
	for j in range(i+1,len(l)):
		if l1[i]==l1[j] and l[i]<l[j]:
			l1[i],l1[j]=l1[j],l1[i]
			l[i],l[j]=l[j],l[i]
		elif l1[i]<l1[j]:
			l1[i],l1[j]=l1[j],l1[i]
			l[i],l[j]=l[j],l[i]
for i in l:
	
	print(i)
