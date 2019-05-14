a,b=map(str,input().split())
s=1
for i in a:
	if i in b:
		s=0
		break
if s==0:
	print("yes")
else:
	print("no")
  #...........
