n=int(input())
if n%2==1:
	print("1")
else:
	for i in range(1,100000):
		d=n//i
		if n%i==0 and d%2!=0:
			print(i)
			break
