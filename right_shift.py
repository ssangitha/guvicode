l=list(map(int,input().split()))
s=[0 for i in range(n)]
x=""
if n<k:
	k=k-n
for i in range(0,n):
	if i+k<len(l):
		s[i+k]=l[i]
	else:
		if len(l)>1:
			a=abs((len(l)-1)-i)
			b=abs(a-k)
			s[b-1]=l[i]
		else:
			s=l
		
for j in s:
	x=x+str(j)+" "
print(x.strip())
