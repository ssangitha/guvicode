n=int(input())
if n<60:
  print("0",n)
elif n==60:
  print("1")
else:
  s=n//60
  r=n%60
  print(s,r)
