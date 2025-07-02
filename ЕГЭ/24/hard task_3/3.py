with open('24.txt') as f:
    s = f.read().split('\n')[:-1]

otv = ''
for i in s:
    d = {}
    for k in range(1, len(i)):
        if i[k - 1] == 'T':
            d[i[k]] = d.get(i[k], 0) + 1
    dd = sorted(d.items(), key=lambda x: (-x[1]))
    ma = dd[0][1]
    dd = list(filter(lambda x: x[1] == ma, dd))
    for i in dd:
        otv += i[0]
g = {}
for i in range(ord('A'), ord("Z") + 1):
    g[chr(i)] = otv.count(chr(i))
print(otv)
print(sorted(g.items(), key=lambda x: -x[1]))
