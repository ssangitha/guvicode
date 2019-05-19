n,k=map(int,input().split())
s=list(map(str,input().split()))
l=s[k:]+s[:k]
print(" ".join(l))
