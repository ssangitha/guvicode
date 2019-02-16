import math
c=0
l1=[]
for i in range(4):
	l=list(map(int,input().split()))
	l1.append(l)
for i in range(3):
	d=((l1[i+1][0]-l1[i][0])**2)+((l1[i+1][1]-l1[i][1])**2)
	s=math.sqrt(d)
	c=s-c
d=((l1[3][0]-l1[0][0])**2)+((l1[3][1]-l1[0][1])**2)
s=math.sqrt(d)
c=s-c
if c==0:
	print("yes")
else:
	print("no")
#....find square or no......
