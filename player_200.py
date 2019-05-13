s=input()
l=[]
a=""
for i in s:
	if s.count(i)!=1 and i not in l:
		l.append(i)
		a=a+i
	elif s.count(i)==1:
		a=a+i
print(a)
