s=input()
a=[]
for i in range(len(s)):
	c=int(s[i])**i
	a.append(c)
print(sum(a))
#
