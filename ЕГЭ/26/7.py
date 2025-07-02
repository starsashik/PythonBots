with open('26 (4).txt') as f:
    data = f.read().split('\n')[1:-1]
data = [list(map(int, x.split(' '))) for x in data]
data = sorted(data, key=lambda x: (x[0], x[1]))
dd = {}
for j in data:
    if j[0] not in dd:
        dd[j[0]] = [j[1]]
    else:
        if j[1] not in dd[j[0]]:
            dd[j[0]] += [j[1]]
res = []
print(dd[27692])
for x, y in dd.items():
    kolvo = 0
    s = ''
    for i in range(len(y) - 1):
        if y[i + 1] - y[i] == 1:
            s += '1'
        else:
            s += '0'
    kolvo = len([k for k in s.split('0') if k and len(k) >= 3])
    res += [[kolvo, x]]
print(sorted(res, key=lambda x: x[0]))
