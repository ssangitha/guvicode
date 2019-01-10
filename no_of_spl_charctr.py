s=input()
l=len(s)
c=0
for i in s:
  if i.isalpha() or i.isdigit():
    c=c+1
print(l-c)
#........no.og.sym.....
