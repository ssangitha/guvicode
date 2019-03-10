n=int(input())
a=""
for i in range(1,n+1):
	if n%i==0 and i%2==0:
		a=a+str(i)+" "
print(a.strip())
#.................even factors........
