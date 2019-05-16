n=int(input())
l=list(map(str,input().split()))
m=[]
for i in range(n):
	m.append(l[i].lower())
m.sort()
for i in range(n):
	print(m[i])
