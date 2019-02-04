n=int(input())
l=[]
s="kabali"
x=0
for i in range(n):
	c=input()
	l.append(c)
for i in l:
	if len(i)==len(s):
		a=i
		for j in a:
			if j in s:
				a=a.replace(j,"0",1)
		if a=="000000":
			x=x+1
print(x)
#.....anagram
