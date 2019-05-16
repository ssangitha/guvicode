n,m=map(int,input().split())
l=list(map(str,input().split()))
a=list(map(str,input().split()))
b=l+a
b.sort()
s=" "
print(s.join(b))
