n,k=map(int,input().split())
l=list(map(str,input().split()))
a=[]
s=" "
for i in l:
	if l.count(i)<k and i not in a:
		a.append(i)
a.sort()
print(s.join(a))
