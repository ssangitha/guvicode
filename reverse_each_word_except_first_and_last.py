s=input()
l=list(s.split(" "))
a=[l[0]]
for i in range(1,len(l)):
	if i==len(l)-1:
		a.append(l[-1])
	else:
		c=l[i]
		b=c[::-1]
		a.append(b)
print(" ".join(a))
#
