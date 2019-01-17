s=input()
a=""
if len(s)%2==1:
	n=len(s)//2
	b=s[n+1:]
	for i in range(n):
		a=a+s[i]
	a=a+"*"+b
else:
	n=len(s)//2
	b=s[n+1:]
	for i in range(n-1):
		a=a+s[i]
	a=a+"**"+b
print(a)
