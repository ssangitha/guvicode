b=int(input())
n=b
while(n!=1):
	if(n&(n-1)==0):
		a=n
		x=0
		break
	else:
		n=n-1
if x==0 and a==b:
	print("0")
else:
	print(b-a)
