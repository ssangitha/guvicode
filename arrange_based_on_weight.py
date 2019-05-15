n=int(input())
h=[]
j=" "
l=list(map(int,input().split()))
m=list(map(int,input().split()))
s=[]
for i in range(n):
	s.append([l[i],m[i]])
s.sort(key=lambda x:x[1])
for i in range(n):
	h.append(str(s[i][0]))
print(j.join(h))
