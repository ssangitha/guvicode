n,k=map(int,input().split())
l=list(map(str,input().split()))
m=l[:k]
n=l[k:]
m.sort()
n.sort(reverse=True)
b=m+n
print(" ".join(b))
