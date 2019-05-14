n=int(input())
s=input()
a=""
c=""
for i in range(n):
	if s[i]!="0":
		a=a+s[i]+" "
	elif s[i]=="0":
		c=c+a
		a=""
print(c.strip())
#........
