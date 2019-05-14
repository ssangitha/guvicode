n=int(input())
s=input()
a=""
c=""
for i in range(len(s)):
	if s[i]=="1":
		a=a+s[i]+" "
	elif s[i]=="0":
		c=c+a
		a=""
print(c.strip())
#........
