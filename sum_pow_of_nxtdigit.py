n=input()
s=0
if len(n)>1:
	a=int(n[0])
	d=int(n[len(n)-1])
	for i in range(0,len(n)-1):
		s=s+(int(n[i])**int(n[i+1]))
	s=s+(d**a)
	print(s)
else:
	print(int(n)**int(n))
	
