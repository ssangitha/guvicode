c=int(input())
n=bin(c)[2:]
a=n[::-1]
for i in a:
	if i=="1":
		print(a.index(i)+1)
		break
