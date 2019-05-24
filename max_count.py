s=input()
x=""
a=[]
b=[]
for i in range(len(s)):
		a.append(s.count(s[i]))
for i in range(len(s)):
	if s.count(s[i])==max(a) and s[i] not in b:
		b.append(s[i])

print(max(a),"".join(b))
