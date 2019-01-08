#........
n=int(input())
j=""
for i in range(1,6):
  s=n*i
  j=j+str(s)+" "
  s=0
x=j.strip()
print(x)
