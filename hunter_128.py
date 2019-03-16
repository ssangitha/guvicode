s=input()
z=[]
for i in range(0,len(s)-1):
	for j in range(i+1,len(s)):
		a=s[i:j+1]
		b=a[::-1]
		if a==b:
			z.append(a)
z.sort(key=len)
for i in z:
	print(i)
