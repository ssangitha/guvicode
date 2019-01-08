def de(l,n):
    if l[0][0]==n:
        l.remove(l[0])
        return l
    elif l[len(l)-1][0]==n:
        l.remove(l[-1])
        l[-1][1]=0
        return l
    else:
        for i in range(len(l)):
            if(l[i][0]==n):
                k=l[i][1]
                l.remove(l[i])
                break
        l[i-1][1]=k
        return l

l=[[10,100],[20,200],[30,300],[40, ]]
print(l)
n=int(input("enter ele to del"))
d=de(l,n)
print(l)
#..........del..list
