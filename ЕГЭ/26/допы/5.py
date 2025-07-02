with open('26-105.txt') as f:
    n, ma = list(map(int, f.readline().split(' ')))
    dd = sorted(list(map(int, f.read().split('\n')[:-1])))
d = []
for i in dd:
    if i + sum(d) <= ma:
        d += [i]
for j in d:
    dd.remove(j)
d1 = d[:len(d) - len(d)//6]
d2 = d[len(d) - len(d)//6:]
d2 = [x * 0.5 for x in d2]
while sum(d1) + sum (d2) < ma - dd[0]/2:
    if (len(d1) + len(d2)) % 6 == 0:
        d2 += [dd.pop(0) * 0.5]
    else:
        d1 += [d2.pop(0) * 2]
        d2 += [dd.pop(0) * 0.5]
print(len(d1) + len(d2), ma - sum(d1) - sum(d2))
print(d1)
print(d2)
