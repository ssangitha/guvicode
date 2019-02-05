s=input()
d=""
for i in s:
	if ord(i)+3<=90:
		d=d+chr(ord(i)+3)
	else:
		a=((ord(i)+3)-90)
		d=d+chr(64+a)
print(d)
#....encoding...
