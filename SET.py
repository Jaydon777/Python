def fun():
    d = {}
    y = list(set(c))
    for i in y:
        d[i] = c.count(i)


    k = 0
    for i in d:
        if d[i] != 1:
            k = 1

    if k != 1:
        print("Unique")
    else:
        for key, value in d.items():
            print(key, ":", value)




l = []
c = []
for i in range(3):
    a = []
    for j in range(3):
        m = (int(input()))
        c.append(m)
        a.append(m)
    l.append(a)

fun()


