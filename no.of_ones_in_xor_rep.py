m,n=map(int,input().split())
p=m|n
c=bin(p)[2:]
print(c.count("1"))
