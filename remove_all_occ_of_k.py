n,k=map(int,input().split())
k=str(k)
s=" "
l=list(map(str,input().split()))
while k in l: 
	l.remove(k)
print(s.join(l))
