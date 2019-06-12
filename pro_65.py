 
a,b= map(int,input().split())
l= list(map(int,input().split()))
amt= int(input())
t= (sum(l)-l[b])//2
if amt == t:
  print("Bon Appetit")
else:
  print(amt-t)
