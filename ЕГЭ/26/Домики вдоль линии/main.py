def ff(n, m):
    global d,li, k
    flag = False
    for j in range(len(d)):
        for h in range(k):
            if d[j][h] < n:
                d[j][h] = m
                flag = True
                break
        if flag:
            break
    if not flag:
        d += [[m, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        li += 1
with open('26_8380.txt') as f:
    k,n = list(map(int, f.readline().split(' ')))
    d = [[0] * k]
    print(d)
    dd = sorted([list(map(int, x.split(' '))) for x in f])
    print(dd)
kolvo = 0
li = 1
gg = 0
for i in dd:
    st = i[0]
    end = i[1]
    ff(st, end)
    if dd.index(i) == len(dd) - 1:
        gg = st
for i in dd:
    for j in i:
        if j > gg:
            kolvo += 1
print(li, kolvo)