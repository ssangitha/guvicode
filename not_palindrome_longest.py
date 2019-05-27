s=input()
n=len(s)
if s!=s[::-1]:
	print(s)
else:
	for i in range(n-1,-1,-1):
		a=s[:i+1]
		if a!=a[::-1]:
			print(a)
			break
