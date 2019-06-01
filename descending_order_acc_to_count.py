n=input()
l=list(map(int,input().split()))
a=[]
b=[]
for i in l:
	if i not in a:
		a.append(i)
		b.append([i,l.count(i)])
b.sort(key=lambda x:x[1],reverse=True)
a=[]
for i in range(len(b)-1):
	for j in range(i+1,len(b)):
		if b[i][1]==b[j][1] and b[i][0]<b[j][0]:
			b[i][0],b[j][0]=b[j][0],b[i][0]
			b[i][1],b[j][1]=b[j][1],b[i][1]
for i in range(len(b)):
	a.append(str(b[i][0]))
print(" ".join(a))
