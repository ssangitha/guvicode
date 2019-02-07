n,k=map(int,input().split())
l=[]
a=["a","e","i","o","u"]
x=0
for i in range(n):
	c=input()
	l.append(c)
for i in l:
	if any(j in a for j in i):
		x=x+1
if x>=k:
	print("yes")
else:
	print("no")
