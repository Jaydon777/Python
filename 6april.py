N = int(input())
M = int(input())
mat = []
for i in range(N):
    mat.append(input().split(' '))
P = [i for i in input()]

def check(lis, P):
    for j in P:
        if j not in lis:
            return False
    return True
x = 0 
for i in mat:
    if check(i, P):
        i.sort()
        for x in i:
            print(x,end='')
        print('')
        print('Lucky Player')
        x = 1

temp = [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

for i in temp:
    if check(i, P):
        i.sort()
        for x in i:
            print(x,end = '')
        print('')
        print('Lucky Player')
        x = 1
if x ==0:
    print('Unlucky Player')