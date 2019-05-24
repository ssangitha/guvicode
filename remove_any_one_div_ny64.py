n=input()
if int(n,2)%64==0:
	print("yes")
else:
	p=1
	for i in range(len(n)):
		s=n[:i]+n[i+1:]
		a=int(s,2)
		if a%64==0:
			print("yes")
			p=0
			break
	if(p==1):
		print("no")
