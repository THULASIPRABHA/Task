l=[1,3,5,7,9]
i=0
b=[]
for i in range(len(l)):
    j=1
    for j in range(0,len(l)):
        a=l[i]*10+l[j]
        b.append(a)
        j=j+1
i=i+1
print("The Two Digit Numbers are=",b)





