n=int(input())
x=""
l=list(map(int,input().split()))
s=[]
for i in l:
	if l.count(i)>1 and i not in s:
		s.append(i)
if len(s)==0:
	print("unique")
else:
	s.sort()
	for i in s:
		x=x+str(i)+" "
	print(x.strip())
#...unique....
