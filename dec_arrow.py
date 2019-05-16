n=int(input())
s="->"
l=list(map(str,input().split()))
l.sort(reverse=True)
print(s.join(l))
