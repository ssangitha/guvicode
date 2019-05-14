n=int(input())
s=input()
a=""
c=""
for i in range(n):
	if s[i]=="1":
		a=a+s[i]+" "
		print(a)
	elif s[i]=="0":
		c=c+a
		a=""
print(c.strip())
#........
