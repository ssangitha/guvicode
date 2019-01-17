s=input()
a=""
for i in s:
	r=int(i)
	if r%2==1:
		a=a+i+" "
b=a.strip()
print(b)
