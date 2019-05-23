n=int(input())
c=0
for i in range(1,n+1):
	if "2" in str(i):
		c=c+1
	if str(i).count("2")>1:
		c=c+(str(i).count("2"))-1
print(c)
