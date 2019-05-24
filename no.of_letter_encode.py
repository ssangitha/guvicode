s=input()
c=1
a=""
if len(s)==1:
	print(s+"1")
else:
	for i in range(len(s)-1):
		if s[i]==s[i+1]:
			c=c+1
		else:
			a=a+s[i]+str(c)
			c=1
	print(a+s[i+1]+str(c))
