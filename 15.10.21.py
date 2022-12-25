'''n=int(input("enter a number:"))
if n>=10:
    sum=0
    sum+=1
    print(sum)
else:
    for i in range (1,n+1):
        fact = 1
        fact=fact*i
    print(fact)'''
'''n= int(input("enter no"))
count=0
while(n>0):
    digit=n%10
    if(digit>1):
        for i in range(2,digit):
            if(digit%1==0):
                count+=1
                break
    elif(digit==1):
        count+=1
    n=n//10
print(count)'''

'''def fact(x):
    print("factors is",x)
    for i in range(1,x+1):
        if (x%i==0):
            print(i)
num = int(input("Enter no"))
fact(num)'''

'''digit = int(input("enter no"))
k = int(input("enter no"))
sum = 0
for digit in str(k):
  sum+=int(digit)
print(sum)'''
# Python program to check if the number is an Armstrong number or not

num = int(input("Enter a number:"))
sum = 0
cal = num
while (cal>0):
  digit = cal%10
  sum+=digit**3
  cal//=10
if sum == num:
  print(num,"is an ARMSTRONG NUMBER")
else:
  print(num,"is NOT AN ARMSTRONG NUMBER")

