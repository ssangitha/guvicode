n=input()
c=0
d=[]
x=[]
for i in range(len(n),0,-1):
	a=n[:i]
	b=a[::-1]
	if a==b:
		d.append(a)
for i in range(1,len(n)+1):
	a=n[i:]
	b=a[::-1]
	if a==b:
		d.append(a)
for i in d:
	x.append(len(i))
j=max(x)
print(len(n)-j)
#.............len of remaining string after deletng longest palindrome.
