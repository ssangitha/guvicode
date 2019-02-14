a,b=map(int,input().split())
c=0
s=a*b
while(s!=0):
	s=s&(s-1)
	c=c+1
print(c)
