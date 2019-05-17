n=int(input())
l=[]
for i in range(0,2**n):
	c=bin(i)[2::]
	k=len(c)
	l.append([(n-k)*"0"+c,c.count("1")])
l.sort(key=lambda x:x[1])
for i in range(len(l)):
	print(l[i][0])
