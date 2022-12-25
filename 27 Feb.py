n = int(input())
lst = []
for i in range(n):
    lst.append(input())
string=""
for i in lst:
    if i == lst[-1]:
        string+=i[0].capitalize()+i[1:]
    else:
        string += i[0].capitalize()+i[1:]+'_'
print(string)