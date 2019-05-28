s=input()
if len(s)%2==0:
	print("NO")
else:
	n=len(s)//2
	a=s[:n]
	b=s[n+1:]
	if a==b:
		print("YES")
	else:
		print("NO")
