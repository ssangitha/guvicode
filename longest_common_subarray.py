a=input()
b=input()
l=[]
m=[]
if a==b:
	print(a)
else:
	for i in range(len(a)):
		for j in range(len(b)):
			c=b[i:j+1]
			if c in a:
				l.append([c,len(c)])
	l.sort(key=lambda x:x[1],reverse=True)
	if l[0][0].isalpha():
		print(l[0][0])
	else:
		for i in range(len(l)):
			if l[i][1]==l[i+1][1]:
				m.append(l[i][0])
				m.append(l[i+1][0])
			else:
				break
		m.sort(reverse=True)
		print(m[0])
				
#common subarray
