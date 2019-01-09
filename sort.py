
#.....sort..........
s=""
n=int(input())
l=list(map(int,input().split()))
min=l[0]
l.sort()
for i in l:
	s=s+str(i)+" "
print(s.strip())
