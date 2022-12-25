m = int(input())
m1 = []
for i in range(m):
    a = int(input())
    i+=1
    m1.append(a)
n = int(input())
n1 = []
for i in range(n):
    b = int(input())
    i+=1
    n1.append(b)

new = m1+n1
a = []
b = []
for i in new:
    if(i%5==0):
        a.append[i]
    else:
        b.append[i]
x = sorted(a)
y = sorted(b)
print(a)
print(b)



