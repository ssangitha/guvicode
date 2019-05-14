n,k=map(int,input().split())
l=list(map(int,input().split()))
m=[]
for i in l:
	if i!=k:
		m.append([i,abs(k-i)])
m.sort(key=lambda x:x[1])
print(str(m[0][0])+" "+str(m[1][0])+" "+str(m[2][0]))
