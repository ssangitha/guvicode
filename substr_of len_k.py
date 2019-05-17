s,k=map(str,input().split())
k=int(k)
l=[]
for i in range((len(s)-k)+1):
	l.append(s[i:i+k])
print(" ".join(l))
