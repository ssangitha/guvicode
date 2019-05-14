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
for i in range(s): 
	b=catalan(i)
	l.append(b)
for i in l:
	x=x+str(i)+" "	
	print(x.strip())
#catalan
