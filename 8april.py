n = int(input())
col = input().split()
m = int(input())
order = input()
for i in col:
    for j in order:
        if list(order[m]) == list(col[i]):
            print("Invalid")
else:
    print("Valid")