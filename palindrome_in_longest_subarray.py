s=input()
c=1
l=[]
if s==s[::-1]:
	print(len(s))
else:
	for i in range(len(s)):
		for j in range(len(s),-1,-1):
			a=s[i:j+1]
			if a==a[::-1]:
				l.append(len(a))
print(max(l))
				
