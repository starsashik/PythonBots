"""def f(x, A):
    return (160 <= x <= 180) <= ((x % 35 == 0) <= (x % A == 0))


for A in range(1, 1000):
    if all([f(x, A) for x in range(1, 10000)]):
        print(A)"""

"""p = {1, 3, 4, 9, 11, 13, 15, 17, 19, 21}
q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
a = set()


def f(x):
    return ((x in p) <= (x in a)) or ((x not in a) <= (x not in q))


for x in range(1, 1000):
    if not f(x):
        a.add(x)


v = 1
for i in a:
    v *= i
print(v)"""

"""def f(x,A):
    return (x % A == 0) or ((x % 23 == 0) <= (x < 50 or x > 70))

for A in range(1, 1000):
    if all(f(x,A) for x in range(1, 10000)):
        print(A)"""

"""p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
q = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
a = set([x for x in range(1, 1000)])


def f(x):
    return ((x in a) <= (x in p)) and ((x in q) <= (x not in a))


for x in range(1, 1000):
    if not f(x):
        a.remove(x)
print(a)
print(len(a))
"""

"""def f(x, A):
    return ((x % 3 != 0) and (x != 48 and x != 52 and x != 56)) <= ((abs(x - 50) <= 7) <= (29 <= x <= 47)) or (x & A == 0)


for A in range(1, 1000):
    if all(f(x,A) for x in range(1, 10000)):
        print(A)"""

"""a = set()

def f(x):
    return (not ((x in [2,4,9,10,15]) == (x in a))) <= ((x in [3,8,9,10,20]) == (x in a))

for x in range(1,1000):
    if not f(x):
        a.add(x)
v = 1
for i in a:
    v *= i
print(v)"""

"""from itertools import product


def f(x):
    return (x not in a) <= ((x in p) or (x not in q))


p = list(product('01', repeat=8))
q = p.copy()
a = set()
res = p.copy()

for i in p:
    w = ''.join(i)
    if w[:2] != '11':
        p.remove(i)
for j in q:
    w = ''.join(j)
    if w[-1] != '0':
        q.remove(j)

for dd in res:
    if not f(dd):
        a.add(dd)

print(len(a))"""