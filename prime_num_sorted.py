n=int(input())
l=[]
s=[]
a=""
for i in range(2,n+1):
	if n%i==0:
		l.append(i)
for i in l:
	for j in range(2,i+1):
		if i%j==0:
			break
	if j==i:
		s.append(j)
for i in s:
	a=a+str(i)+" "
print(a.strip())
		#....print the sorted prime number from the factors of number..
