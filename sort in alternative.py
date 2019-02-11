n=int(input())
d=[]
s=""
l=list(map(int,input().split()))
l.sort()
while(len(l)>1):
	d.append(l[-1])
	d.append(l[0])
	l.remove(l[0])
	l.remove(l[-1])
d=d+l
for i in d:
	s=s+str(i)+" "
print(s.strip())
