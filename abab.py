a=input()
b=input()
c=0
x=0
for i in range(len(a)):
    s=a[:i+1]
    for j in range(0,len(b),len(s)):
        if s==b[j:j+len(s)]:
            x=1
        else:
            x=0
    if x==1 and j==len(b)-len(s):
        c=c+1
print(c)
        
