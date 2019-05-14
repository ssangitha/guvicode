def catalan(n): 
    if n <=1 : 
        return 1
    res = 0 
    for i in range(n): 
        res += catalan(i) * catalan(n-i-1) 
  
    return res 
s=int(input())
l=[]
x=""
if s==2:
	print("1 1")
else:
	for i in range(s+1): 
		b=catalan(i)
		l.append(b)
	for i in l:
		x=x+str(i)+" "	
	print(x.strip())
