e1,f=map(int,input().split())
if e1<=f:
  g=e1
else:
  g=f
x=[]
for i in range(0,g):
  x.append(sorted(list(map(int,input().split()))))
x=sorted(x)
for i in range(0,len(x[0])):
  for j in range(0,len(x)-1):
    if x[j][i]>x[j+1][i]:
      x[j][i],x[j+1][i]=x[j+1][i],x[j][i]
for i in x:
  print(*i)
  #...
