s=input()
i=1
if len(s)==1:
	print("yes")
else:
	for j in s:
		if s.count(j)==len(s):
			print("no")
			i=0
			break
	if i==1:
		print("yes")
			
