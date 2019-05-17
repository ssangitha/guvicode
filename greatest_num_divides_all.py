n=int(input())
l=list(map(int,input().split()))
s=[]
d=0
for i in range(n):
	for j in range(n):
		if l[j]%l[i]==0:
			d=1
		else:
			d=0
			break
	if d==1:
		s.append(l[i])
print(max(s))
