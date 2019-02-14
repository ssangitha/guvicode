l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=list(map(int,input().split()))
if (l1[0]==l2[0] and l2[0]==l3[0]) or (l1[1]==l2[1] and l2[1]==l3[1]) or (l1[0]==l1[1] and l2[0]==l2[1] and l3[0]==l3[1]):
	print("yes")
else:
	print("no")
