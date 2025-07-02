f = open('26_9077.txt')
m, n = list(map(int, f.readline().split(' ')))
dd = [list(map(int, x.split(' '))) for x in f]
dd.sort()

z = [[0] * 1500 for x in range(m)]

for st, dt, x, y in dd:
    z[x - 1][st] -= 1
    z[y - 1][st + dt] += 1

k = mt = 0

for t in range(1500):
    for i in range(m):
        k += z[i][t]
    mt = min(mt, k)

p = [0] * m
for i in range(m):
    k = 0
    for t in range(1500):
        k += z[i][t]
        p[i] = min(p[i], k)
print(-sum(p), -mt)