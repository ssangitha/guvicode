s=input()
c=0
l=[]
for i in range(len(s)-1):
	if int(s[i])%2==0 and int(s[i+1])%2==1:
		c+=1
	elif int(s[i])%2==1 and int(s[i+1])%2==0:
		c+=1
	else:
		l.append(c)
		c=0
l.append(c)
a=max(l)
if a==0:
	print("0")
else:
	print(a+1)
