a,b=map(str,input().split())
c=max(len(a),len(b))
s=0
for i in range(c):
	if a[i]!=b[i]:
		s=s+1
	if s>1:
		break
if s==1:
	print("yes")
else:
	print("no")
#......string differ by one character....
