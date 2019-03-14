n=int(input())
a="1 "
for i in range(3,n+1):
	if n%i==0 and i%2==1:
		a=a+str(i)+" "
print(a.strip())
#odd factors...
