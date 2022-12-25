
import random

print("Click ENTER to roll dice")
x=input()
flag=True
while flag==True:
    number=random.randint(1,6)
    if number==1:
        print("\n   o  \n" )
    if number==2:
        print("o   \n \n    o")
    if number==3:
        print("o   \n  o  \n    o")
    if number==4:
        print("o   o\n  \no   o")
    if number==5:
        print("o   o\n  o \no   o" )
    if number==6:
        print("o o o\n \no o o")
       

    print("Type YES to roll again or NO to exit")
    a=input()
    if a=="YES":
        flag=True
    else:
        flag=False
        break
