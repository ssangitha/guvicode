s=input()
a=""
x=s.count(s[0])
for i in s[1:]:
	m=s.count(i)
	if m<x:
		x=m
for i in s:
	if s.count(i)==x and i!=" ":
		a=a+i+" "
print(a.strip())
