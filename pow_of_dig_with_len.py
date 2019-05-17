n=input()
s=[]
l=len(n)
for i in n:
	s.append(int(i)**l)
print(sum(s))
