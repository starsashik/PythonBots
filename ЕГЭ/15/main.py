from itertools import *


def f(x):
    P = 23 <= x < 45
    Q = 34 <= x <= 56
    A = a1 <= x <= a2
    return (not A) or ((not P) and Q)


res = []
Ox = [i / 4 for i in range(4 * 23, 57 * 4)]
for a1, a2 in combinations(Ox, 2):
    if all(f(x) for x in Ox):
        res.append(a2 - a1)
print(max(res))
