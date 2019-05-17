s=input()
a=[]
if s=="1":
	print("1")
else:
	for i in range(len(s)):
		c=int(s[i])**i
		a.append(c)
	print(sum(a))
