s=input()
a=""
l=""
for i in s:
	if i!=" ":
		a=a+i
	elif i==" ":
		l=l+a[::-1]+" "
		a=""
print(l+a[::-1])
