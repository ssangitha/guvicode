#.....sort..........
n=int(input())
l=list(map(int,input().split()))
min=l[0]
for i in range(1,n):
  if min>l[i]:
    l[i],l[i+1]=l[i+1],l[i]
print(l)
