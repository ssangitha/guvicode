a=['0','1','2','3','4','5','6','7','8','9','.']
s=input()
for i in range(0,len(s)):
  if s[i] not in a:
    print("No")
    break
if(i==(len(s)-1)):
  print("Yes")
#........num.....
