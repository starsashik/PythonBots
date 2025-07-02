with open('26_7626.txt') as f:
    k = int(f.readline())
    d = [-1] * k

    n = int(f.readline())
    dd = sorted([list(map(int, f.readline().split(' '))) for x in range(n)])

kolvo = 0
cur = 0
for x in dd:
    start, end = x
    for j in range(k):
        if start > d[j]:
            d[j] = end
            cur = j + 1
            kolvo += 1
            break
print(kolvo, cur)