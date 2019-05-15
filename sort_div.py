a,b=map(int,input().split())
s=""
l=list(map(int,input().split()))
l.sort()
for i in l:
	s=s+str(i)+" "
print(s.strip())
