s=""
n,m=map(int,input().split())
for i in range(n+1,m):
  if i%2!=0:
    s=s+str(i)+" "
r=s.strip()
print(r)
    
