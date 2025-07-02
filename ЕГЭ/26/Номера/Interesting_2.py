# 7855
with open('26_5.txt') as f:
    k = int(f.readline())
    d = [(x + 1, 0) for x in range(k)]

    n = int(f.readline())
    dd = [list(map(int, x.split(' '))) for x in f]
    dd = sorted(dd, key=lambda x: (x[0], x[1]))

nomer = 0
tim = 0

for i in dd:
    st = i[0]
    end = i[1]
    j = d.index(sorted(d, key=lambda x: (x[1], -x[0]))[0])
    tim = max(tim, d[j][1] + 31 - st)
    d[j] = (j + 1, end)
    if end <= 10080:
        nomer = j + 1
print(tim, nomer)
