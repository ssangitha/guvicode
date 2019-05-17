s=input()
m=s.count("@")
a=s.count(".")
for i in range(len(s)-2):
	if s[i]=="@":
		x=s[:i]
		b=i
	if s[i]==".":
		y=s[b+1:i]
if m==1 and a==1 and len(x)>=3 and len(y)>=4 and s[len(s)-4:]==".com":
	print("YES")
else:
	print("NO")
