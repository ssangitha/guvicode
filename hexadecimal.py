s=input()
for i in s:
	if i<="9" or i<="F":
		a=0
	else:
		a=1
		break
if a==0:
	print("yes")
else:
	print("no")
