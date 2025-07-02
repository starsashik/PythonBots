#8168 хз что со временем
with open('26_6.txt') as f:
    k = int(f.readline())
    d = [[0] *1441 for i in range(k)]
    print(d)

    n = int(f.readline())
    dd = sorted([list(map(int, x.split(' '))) for x in f], key=lambda x:(x[0], x[1]))
kolvo = 0
for i in dd:
    st = i[0]
    end = i[1]
    flag = False
    for j in range(len(d)):
        if all(not d[j][x] for x in range(st, st + end+ 1)):
            d[j][st+ 1:st+end+1] = [1] * (end)
            print(len(d[j]))
            flag = True
            break
    if not flag:
        kolvo += 1
print(kolvo)
tim = 0
for i in range(1441):
    if all(d[l][i] for l in range(k)):
        tim += 1
print(tim)