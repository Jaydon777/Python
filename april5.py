# n = input().split(' ')
# n1 = []
# for i in n:
#     n1.append(int(i)//2)
# n2 = list(set(n1))
# print(n2)
# sum = 0
# for i in range(len(n2)-1):
#     a = n2[i:i+2]
#     print(a, end = ' ')
#     for j in a:
#         sum+=j
#         print(sum,end = ' ')

    
# print(nxt)
# A = [1, 2, 3, 4, 5]
# sum=0
# for i in range(len(A) - 1):
#     value = A[i:i+2]
#     print(va)
#     for j in value:
#         sum+=j
#         print(sum)

l = input().split(' ')
sum=0
for i in range(len(l)):
    sum+=int(l[i])
s=sum/4
E = s-(int(l[2])+int(l[3]))
B = s-(int(l[5])+int(l[6]))
C = s-(int(l[0])+int(l[9]))
A = s-(int(l[4])+int(l[8]))
D = s-(A+B+C+E)
print(int(A),int(B),int(C),int(D),int(E))
