from itertools import permutations
n=input()
c=0
k=len(n)
x=list(permutations(n,k))
l=[]
for i in range(len(x)):
	l.append(int("".join(x[i])))
l.sort()
for i in range(len(l)-1):
	if l[i]==int(n):
		print(l[i+1])
		c=1
		break
if c==0:
	print("impossible")
