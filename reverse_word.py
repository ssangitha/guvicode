s=input()
c=s.count(" ")
x=""
for i in range(c+1):
	if c>=1:
		a=s.index(" ")
		s1=s[:a]
		s=s[a+1:]
		x=x+s1[::-1]+" "
		c=s.count(" ")
		
	else:
		x=x+s[::-1]
print(x.strip())
#............reverse the word.........
