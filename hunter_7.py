n=int(input())
l=list(map(int,input().split()))
z=[]
a=""
for i in range(n):
	if i%2==0 and l[i]%2==1:
		z.append(str(l[i]))
	elif i%2==1 and l[i]%2==0:
		z.append(str(l[i]))
for i in z:
    a=a+i+" "
print(a.strip())
