n=int(input())
for i in range(2,n):
  if n%i==0:
    break;
if(i==n):
  print("no")
else:
  print("yes")
