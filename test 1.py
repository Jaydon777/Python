a=[]
c=[]
n1=int(input("Enter number of elements for list 1:"))
for i in range(1,n1+1):
    b=int(input("Enter element:"))
    a.append(b)
n2=int(input("Enter number of elements for list 2:"))
for j in range(1,n2+1):
    d=int(input("Enter element:"))
    c.append(d)
lst =a+c
print(lst)
