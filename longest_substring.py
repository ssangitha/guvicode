s,p=map(str,input().split())
b=""
for i in range(1,len(p)+1):
	a=p[0:i]
	if a in s:
		b=b+p[i-1]
print(b)
