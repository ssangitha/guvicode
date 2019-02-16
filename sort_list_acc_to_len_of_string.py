n=int(input())
l=list(map(str,input().split()))
d=sorted(l,key=len)
if n>1:
	for i in range(n-1):
		if len(d[i])==len(d[i+1]) and d[i]>d[i+1]:
			d[i],d[i+1]=d[i+1],d[i]
		else:
			break
	print(" ".join(d))
else:
	print(l[0])
  #...................sort..........
