n=int(input())
l=list(map(int,input()))
max=l[0]
for i in range(1,n):
  if max<l[i]:
    max=l[i]
print(max)
