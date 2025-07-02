from itertools import combinations

with open('27991_A.txt') as f:
    n = int(f.readline())
    dd = list(map(int, f.read().split('\n')))
otv = (0, 0)
ma = 0

for x, y in combinations(dd, 2):
    if (x - y) % 2 == 0 and x * y % 17 == 0:
        if ma < x + y:
            ma = x + y
            otv = (x, y)

print(otv)

# Эффективный способ
f = open('27991_B.txt')
n = int(f.readline())
ch_17 = [0, 0]
nch_17 = [0, 0]
ch_0 = 0
nch_0 = 0
for i in f.readlines():
    x = int(i)
    if x % 2 == 0:
        if x % 17 == 0:
            ch_17.append(x)
            ch_17.sort()
            ch_17.pop(0)
        else:
            ch_0 = max(x, ch_0)
    else:
        if x % 17 == 0:
            nch_17.append(x)
            nch_17.sort()
            nch_17.pop(0)
        else:
            nch_0 = max(x, nch_0)

res = max(sum(ch_17), sum(nch_17), max(ch_17) + ch_0, max(nch_17) + nch_0)
for x, y in combinations(ch_17 + nch_17 + [ch_0, nch_0], 2):
    if x + y == res:
        print(x, y)
