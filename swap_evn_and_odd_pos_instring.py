s=input()
a=[]
b=[]
c=""
for i in range(len(s)):
	if i%2==0:
		a.append(s[i])
	else:
		b.append(s[i])
for i in range(len(s)//2):
	c=c+b[i]+a[i]
print(c)
#......swap...
