x,k=map(int,input().split())
c=x^k
s=bin(c)[2:]
print(s.count("1"))
