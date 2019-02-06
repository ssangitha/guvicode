n=int(input())
l=list(map(int,input().split()))
s=[]
x=""
if all(i is 0 for i in l):
	print("0")
else:
	for i in range(len(l)):
		a=max(l)
		l.remove(a)
		s.append(a)
	for i in s:
		x=x+str(i)
	print(x.strip())
  #....largest num...
