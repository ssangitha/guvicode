#.....min..........
n=int(input())
l=list(map(int,input().split()))
min=l[0]
for i in range(1,n):
  if min>l[i]:
    min=l[i]
print(min)
