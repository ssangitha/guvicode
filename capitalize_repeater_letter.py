s=input()
a=""
for i in s:
	if s.count(i)==1 or i==" ":
		a=a+i
	else:
		a=a+i.upper()
print(a)
