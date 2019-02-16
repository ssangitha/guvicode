a,b,c=map(str,input().split())
c=int(c)
x=0
for i in range(len(b)):
	if a[i]!=b[i]:
		x=x+1
	if x>c:
		break
if x==c:
	print("yes")
else:
	print("no")
