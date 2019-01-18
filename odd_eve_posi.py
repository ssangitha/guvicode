s=input()
a=""
b=""
for i in range(0,len(s),2):
	a=a+s[i]
for i in range(1,len(s),2):
	b=b+s[i]
print(a,b)
