a=input()
b=input()
l=[]
if a==b:
	print(a)
else:
	for i in range(len(a)):
		for j in range(len(b)):
			c=b[i:j+1]
			if c in a:
				l.append([c,len(c)])
l.sort(key=lambda x:x[1],reverse=True)
print(l[0][0])
