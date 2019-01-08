#.......prime nums....
s=""
n,m=map(int,input().split())
for i in range(n+1,m):
  for j in range(2,i+1):
    if i%j==0:
      break
  if i==j:
    s=s+str(i)+" "
r=s.strip()
print(r)
