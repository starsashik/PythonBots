from functools import lru_cache

"""def f(start, finish, meet29=False):
    if start == 29:
        meet29 = True
    if start == finish and meet29:
        return 1
    if start > finish:
        return 0
    return f(start + 2, finish, meet29) + f(start + sum([int(x) for x in str(start)]), finish, meet29)


print(f(3, 68))
"""

"""data = set()
def f(s):
    if s > 100:
        return
    if s % 2 == 0:
        data.add(s)
    f(s + 3)
    f(s * 3)
f(3)
print(len(data))"""

"""@lru_cache(None)
def f(s, fi):
    if s == fi:
        return 1
    if s > fi:
        return 0
    res = f(s + 5, fi) + f(s + 10, fi)
    if s % 10 != 0 and s % 10 != 1:
        res += f(s * (s % 10), fi)
    return res
print(f(10, 220))"""

"""def f(start, finish, meet25=False):
    if start == 25:
        meet25 = True
    if start == finish and meet25:
        return 1
    if start > finish:
        return 0
    return f(start + 1, finish, meet25) + f(start * 2, finish, meet25) + f(start + start + 1 + 1 * (start % 2), finish,
                                                                           meet25)


print(f(3, 75))"""

"""def f(start, finish, num = 0):
    if num > 1:
        return 0
    if start == finish and num == 1:
        return 1
    if start == finish and num == 0:
        return 0
    if start > finish:
        return 0
    return f(start+1, finish, num) + f(start + 2, finish, num) + f(start*2, finish, num + 1)
print(f(2, 12))"""

"""res = set()
@lru_cache(None)
def f(start, finish, num=0):
    if start == finish:
        res.add(num)
        return
    if start > finish or num > 30:
        return
    f(start + 1, finish, num + 1)
    f(start*2,finish, num + 1)
    f(start * 3, finish, num + 1)

f(1, 32718)

print(res)"""

# Интересная задача
"""def f(start, finish, data=frozenset()):
    if start in data or start > 50 or start < 0:
        return 0
    if start == finish:
        return 1
    return f(start * 3, finish, data | {start}) + f(start - 3, finish, data | {start})

print(f(3,30))"""

"""def ff(s):
    s = int(s, 2) + 1
    return bin(s)[2:]


def f(start, finish):
    if start == finish:
        return 1
    if int(start,2) > int(finish,2):
        return 0
    return f(start + '0',finish) + f(start + '1', finish) + f(ff(start), finish)


print(f('100', '11101'))"""

"""def f(start, finish, op=''):
    if start == finish:
        return 1
    if start > finish:
        return 0
    res = f(start + 1, finish) + f(start * 2, finish)
    if op != '+3':
        res += f(start + 3, finish, '+3')
    return res
print(f(2, 20))
"""

"""res = set()


def f(start,num=0):
    if num == 9:
        res.add(start)
        return
    f(start * 2, num + 1)
    f(start * 2 + 1, num + 1)

f(1)
print(len(res))"""

"""def f(start, finish):
    if start == finish:
        return 1
    if start > finish:
        return 0
    res = 0
    if start % 10 != 0:
        res += f(start + start % 10, finish)
    if start >= 20:
        res += f(start * (start // 10), finish)
    if str(start)[0] != str(start)[1]:
        res += f(start + abs(start % 10 - start // 10), finish)
    return res


print(f(21, 62))"""

# Тоже интересная задача
"""def f(start):
    if start == 8:
        return 1
    if start < 10:
        return 0
    return f(start % 10 + start // 10) or f((start % 10) * (start // 10))


k = 0
for i in range(10, 100):
    if f(i):
        k += 1
print(k)"""
