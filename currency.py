n=int(input())
l=[1000,500,100,50,10,1]
c=0
while n!=0:
	for i in l:
		if n>=i:
			n=n-i
			c+=1
			break
print(c)
