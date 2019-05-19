s=input()
l=list(s.split(" "))
if s=="and":
	print("and")
else:
	for i in range(len(l)):
		if l[i]=="and":
			l[i-1],l[i+1]=l[i+1],l[i-1]
	print(" ".join(l))
