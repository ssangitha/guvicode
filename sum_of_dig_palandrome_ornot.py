n=input()
s=0
for i in n:
	s=s+int(i)
a=str(s)
b=a[::-1]
if a==b:
	print("YES")
else:
	print("NO")
