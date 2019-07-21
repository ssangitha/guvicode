n,m=map(int,input().split())
l=list(map(int,input().split()))
d=0
lo=0
while m>0:
  m=m-86400+l[lo]
  d+=1
  lo+=1
print(d)
