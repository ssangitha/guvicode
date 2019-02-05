# your code goes here
n=int(input())
l=[]
s=sorted("kabali")
x=0
for i in range(n):
	c=input()
	l.append(c)
for i in l:
	if len(i)==len(s):
		a=sorted(i)
		if s==a:
			x=x+1
print(x)
#.....anagram
