#
n1,n2,n3,n4=map(int, input().split())
c=0
d=n2-n3
if (d>=0):
    s=(n1-n3)*2
    for i in range (n4):
        if (i==n4-1):
             s=s/2
        if (d<s):
            d=n2
            c+=1
        d=d-s
        if (d<0):
            c=-1
            break
        s=2*n1-s
    print(c)
else:
    print(-1)
