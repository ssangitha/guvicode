n=int(input())
l=list(map(str,input().split()))
if n%2==0:
	h=(n-1)//2
else:
	h=(n-2)//2
l1=l[:h+1]
l1.sort()
l2=l[h+1:]
l3=sorted(l2,reverse=True)
print(" ".join(l1+l3))
