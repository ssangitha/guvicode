a,k=map(int,input().split())
s=0
i=""
for n in range(a+1,k):
  m=n
  while n>0:
    r=n%10
    s=s+(r*r*r)
    n=n//10
  if(m==s):
    i=i+str(s)+" "
    s=0
  else:
  	s=0
x=i.strip()
print(x)
#......arm....
