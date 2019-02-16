a,b=map(str,input().split())
for i in range(len(a)-1):
	c=a[i:i+2]
	if c in b:
		print("yes")
		break
if i ==len(a)-2:
	print("no")
 #....substring present or not.....
