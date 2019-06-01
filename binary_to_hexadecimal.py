s=input()
bin=int(s,2)
o=hex(bin)[2:]
a=""
for i in o:
	if i.isalpha():
		a=a+i.upper()
	else:
		a=a+i
print(a)
