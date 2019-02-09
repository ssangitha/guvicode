s=input()
x=0
for i in s:
	if int(i)%2==1:
		x=x+int(i)
if x%2==0:
	print("E")
else:
	print("O")
