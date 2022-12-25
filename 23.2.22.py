import copy
r = int(input(''))
c = int(input(''))
lis1=[]
for i in range(r):
    lis1.append(input('').split(' '))
for i in lis1:
    for j in range(len(i)):
        i[j] = int(i[j])

lis2 = copy.deepcopy(lis1)
for i in range(len(lis1)):
    for j in range(len(lis1[i])):
        lis2[i][j]+=max(lis1[i])


lis3 = [[lis1[j][i] for j in range(len(lis1))] for i in range(len(lis1[0]))]
lis4 = copy.deepcopy(lis3)
for i in range(len(lis3)):
    for j in range(len(lis3[i])):
        lis4[i][j]=min(lis3[i])
lis5 = [[lis4[j][i] for j in range(len(lis4))] for i in range(len(lis4[0]))]

for i in range(len(lis2)):
    for j in range(len(lis2[0])):
        lis2[i][j]+= lis5[i][j]

for i in lis2:
    for j in i:
        print(j,'', end='')
    print('')