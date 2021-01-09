import random
b=[]                        
lst=[]
while len(b)<4:        
    n = random.randint(1,9) 
    if n not in b:
        b.append(n)
while lst!=b:
    lst.clear()
    for j in range(0, len(b)):
        l = int(input("Enter the element one by one="))
        if l not in lst:
            lst.append(l)
    
    for i in range(0,len(lst)):
        if lst[i]==b[i] :
            print(lst[i],"-C")
            
        elif lst[i] in b:
            print(lst[i],"-P")
            
        else:
            print(lst[i],"-X")

i=i+1
print("Hurray You Got it")

            
    
   


