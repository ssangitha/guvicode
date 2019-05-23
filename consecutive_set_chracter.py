s=input()
c=1
a=[]
for i in range(len(s)-1):
	if s[i]==s[i+1]:
		c=c+1
	else:
		a.append([s[i],c])
		c=1
a.append([s[i],c])
a.sort(key=lambda x:x[1])
print(a[-1][0],a[-1][1])
