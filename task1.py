l1= ['stephen', 'muthu', 'celin', 'rajarajan']
s = [18, 22.3, 19.1, 17.2]
length=len(s)
for x in range(length):
    for y in range(x,length):
        if s[x]>s[y] :
            s[x],s[y]=s[y],s[x]
            l1[x],l1[y]=l1[y],l1[x]
for x in range(length):
        print(l1[x],"=" ,s[x])
        
