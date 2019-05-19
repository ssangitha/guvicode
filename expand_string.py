s=input()
a=[]
c=""
g=""
for i in s:
	if i.isalpha():
		a.append(i)
		g=g+" "
	else:
		g=g+i
g=g[1:]
d=list(g.split(" "))
for i in range(len(d)):
	if int(d[i])%2==0:
		c+=(a[i]*int(d[i]))
	else:
		c+=a[i]+d[i]
print(c)
