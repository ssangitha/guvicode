n=input()
p=1
for i in range(len(n)):
	s=n[i:]
	a=int(s,2)
	if a%64==0:
		print("yes")
		p=0
		break
if(p==1):
	for i in range(len(n)):
		s=n[:1+1]
		a=int(s,2)
		if a%64==0:
			print("yes")
			p=0
		    break
if p==1:
	print("no")
