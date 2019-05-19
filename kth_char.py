s,k=input().split()
k=int(k)
a=s[k-1]+" "
for i in range(k-1,len(s)-k,k):
	a+=s[i+k]+" "
print(a.strip())
	
