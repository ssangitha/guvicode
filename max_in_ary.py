n=int(input())
l=[]
for i in range(n):
  c=int(input())
  l.append(c)
max=l[0]
for i in range(1,n):
  if max<l[i]:
    max=l[i]
print(max)
