l=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
s=input()
a=input()
x=""
for i in range(len(s)):
	c=l.index(s[i])+l.index(a[i])+1
	if c<=25:
		x=x+l[c]
	else:
		d=c%26
		x=x+l[d]
print(x)
