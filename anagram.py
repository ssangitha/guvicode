n=int(input())
l=[]
s="Kabali"
x=0
for i in range(n):
	c=input()
	l.append(c)
for i in l:
	if len(i)==len(s):
		a=i
		for j in s:
			if j in a:
				a.replace(j,"")
		if len(a)==0:
			c=c+1
print(c)
