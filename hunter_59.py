n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
x=""
for i in range(n):
	c.append(a[i]+b[i])
for i in c:
	x=x+str(i)+" "
print(x.strip())
