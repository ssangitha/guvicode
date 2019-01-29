n=int(input())
s=input()
a=["a","e","i","o","u"]
x=""
for i in s:
	if i not in a:
		x=x+i
print(x[::-1])
#....eliminate vowels and reverse it...
