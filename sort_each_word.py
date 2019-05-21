s=input()
l=list(s.split(" "))
a=[]
for i in l:
	b=sorted(i)
	a.append("".join(b))
print(" ".join(a))
