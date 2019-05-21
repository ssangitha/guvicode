a=input()
d=[]
s=[]
r=""
for i in a:
	if i.isdigit():
		d.append(int(i))
	else:
		s.append(i)
for i in range(len(d)):
	r=r+(s[i]*d[i])
print(r)
