n=int(input())
l=list(map(int,input().split()))
s=[]
x=""
for i in range(len(l)):
	if i==l[i]:
		s.append(l[i])
if len(s)==0:
	print("-1")
else:
	for i in s:
		x=x+str(i)+" "
	print(x.strip())
#.........print the elements if index equal to value............
