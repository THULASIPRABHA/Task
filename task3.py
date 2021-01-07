name = input("Enter Your Name=")
d = {}
for i in name:
     d[i] = d.get(i,0)+1
for x,y in d.items():
    print(x,"occur",y,"times")
greater = dict((x, y) for x, y in d.items() if y >1)
print ("The value greater than 1 is printed here=",greater)
equal = dict((x, y) for x, y in d.items() if y ==1)
print ("The value equal to 1 is printed here=",equal)
print(sorted([x,"is the highest occur in",y,"times"]for x,y in d.items())[0])
