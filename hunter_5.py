s=input()
c=1
for i in range(len(s)-1):
	a=s[i]+s[i+1]
	x=int(a)
	if x<=26 and s[i]!="0":
		c+=1
if c==3:
	print(c)
else:
	print(c+(c-1)//2)
