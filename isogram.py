s=input()
for i in range(0,len(s)):
	c=s.count(s[i])
	if c!=1:
		print("No")
		break
if i==len(s)-1:
	print("Yes")
