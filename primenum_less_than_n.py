n=int(input())
a=""
if n==2:
	print("0")
else:
	for i in range(2,n):
		for j in range(2,i+1):
			if i%j==0:
				break
		if i==j:
			a=a+str(i)+" "
	print(a.strip())
#..........prime....
