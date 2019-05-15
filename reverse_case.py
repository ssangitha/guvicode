s=input()
a=""
for i in s:
	if i.islower():
		a=a+i.upper()
	elif i.isupper():
		a=a+i.lower()
	else:
		a=a+i
print(a)
