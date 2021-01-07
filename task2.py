hr=int(input("Enter the your work hour="))
salary=100
if hr >60:
    print("sorry! OT amount only for 60hrs")
    print("your OT amount is=",(20)*salary*1.5)
    print("your weekly salary with OT is ",40*salary +(20)*salary*1.5)
else :
    print("your OT amount is=",(hr-40)*salary*1.5)
    print("your weekly salary with OT is ",40*salary +(hr-40)*salary*1.5)

