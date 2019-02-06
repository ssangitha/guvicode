n=int(input())
l=list(map(int,input().split()))
for i in l:
	if l.count(i)==1:
		print(i)
 #....print the number which appear only once....
