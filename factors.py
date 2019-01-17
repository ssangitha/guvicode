n=int(input())
a="1 "
for i in range(2,(n//2)+1):
	if n%i==0:
		a=a+str(i)+" "
a=a+str(n)
print(a)
