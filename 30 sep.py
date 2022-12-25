'''a = int(input("Enter number:"))
b = int(input("Enter number:"))
prod = a*b
print(prod) '''

'''a = float(input("Enter number:"))
b = float(input("Enter number:"))
prod = a*b
print(int(prod)) '''

'''a = int(input("Enter number:"))
squ = a**2
print(squ)'''


'''a = int(input("Enter number:"))
b = int(input("Enter number:"))
c = int(input("Enter number:"))
s = (a/2+(b*c)*2)
print(s)'''



'''a = int(input("Enter number:"))
b = int(input("Enter number:"))
c = int(input("Enter number:"))
d = int(input("Enter number:"))
s = (a-d+(b*(c//3))*2)
print(s)'''

#****************************************************************************
'''A=int(input("Enter a number:"))
if A%2==0:
    print(A,"is even")
else:
    print(A,"is odd")'''

'''M = int(input("Enter math score:"))
P =  int(input("Enter physics score:"))
C = int(input("Enter chemistry score:"))
avg = (M+P+C)/3
if avg >=98:
    print("candidate is eligible for medical education")
else:
    print("candidatte is eligible for engineering education")'''

'''a = int(input("Enter number:"))
b = int(input("Enter number:"))
c = int(input("Enter number:"))
if a>b:
    if a>c:
        print(a,"is the greater")
    else:
        print(c,"is greater")
elif b>c:
        print(b,"is greater")
else:
    print(c,"is graeter")'''

# Python program to check if year is a leap year or not

'''year = int(input("Enter the year:"))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print(year," is a leap year")
       else:
           print(year," is not a leap year")
   else:
       print(year," is a leap year")
else:
   print(year,"is not a leap year")'''

##

'''count = int(input("Enter how many times to say hello:"))
i = 1
while i<=count:
   print("hello")
   i+=17
print("done!!")'''


'''i = 1
sum = 0
while i<=10:
   sum+=1
   i+=1
   print(sum,end = ' ')
print(sum,'\n')'''

'''n=int(input("enter no"))
for i in range(0,n):
   print("\n")
   for j in range(0,i+1):
      print("*",end='')'''

'''for i in range(10):
   print('#',(i+1))'''

sum=0
for i in range(0,51,5):
   sum+=i
print(sum)



