'''import math
def mat(x):
    y = math.asin(x)
    p = 57.2958 * y
    print(p)

num = float(input("Enter the value to be calculated:"))
mat(num)'''

    
n=int(input('enter'))
wrds=input('enter')
lis=wrds.split(' ')
score=0
def vow_calc(word):
    vows=['a','e','i','o','u']
    cnt=0
    for letter in word:
        if vows.count(letter) == 1:
            cnt+=1
    if cnt%2 == 0:
        return 2
    return 1

for i in lis:
    score+=vow_calc(i)
    print(vow_calc(i))
print(score)
