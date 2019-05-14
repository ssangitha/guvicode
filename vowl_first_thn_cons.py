s=input()
l=["a","e","i","o","u"]
a=""
b=""
for i in s:
	if i in l:
		a=a+i
	else:
		b=b+i
print(a+b)
