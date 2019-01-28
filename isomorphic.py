a,b=map(str,input().split())
c=[]
d=[]
for i in a:
	c.append(a.count(i))
for j in b:
	d.append(b.count(j))
if all(i in d for i in c):
	print("yes")
else:
	print("no")
#...isomorpic.....
