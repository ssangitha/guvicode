# your code goes here
n=input()
if any(i.isalpha() for i in n):
	if any(i.isdigit() for i in n):
		print("Yes")
	else:
		print("No")
else:
	print("No")
			
			
