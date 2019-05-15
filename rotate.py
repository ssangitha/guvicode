s,n=input().split()
c=int(n)
l=[0]*len(s)
for i in range(len(s)):
	if i+c<=len(s)-1:
		l[i+c]=s[i]
	else:
		l[i%c]=s[i]
print("".join(l))
