s=input()
d=""
for i in s:
	if i not in d:
		d=d+i
print(d[::-1])
