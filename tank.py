n=int(input())
li=[]
a=n//2+n
for i in range(1,n+1):
    if i%2==0:
        li.append(i)
for i in range(1,n+1):
    if i%2!=0:
        li.append(i)
for i in range(1,n+1):
    if i%2==0:
        li.append(i)
print(a)
print(*li)
