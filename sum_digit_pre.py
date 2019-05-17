n=input()
s=[]
d=[]
for i in range(len(n)):
	c=n[:i+1]
	for j in c:
		d.append(int(j))
		s.append(sum(d))
		d=[]
print(sum(s))
#
