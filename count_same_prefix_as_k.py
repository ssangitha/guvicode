n=int(input())
l=list(map(str,input().split()))
p=input()
c=0
a=len(p)
for i in l:
	if i[:a]==p:
		c+=1
print(c)
