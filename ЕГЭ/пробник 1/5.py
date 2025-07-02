from functools import lru_cache
from itertools import product

#
# def f(x,y,z):
#     return ((not x) and y and z) or ((not x) and (not y) and z) or ((not x) and (not y) and (not z))
#
#
# print("x y z")
# for x,y,z in product([0,1], repeat=3):
#     if f(x,y,z):
#         print(x,y,z)
#
# """
# x y z
# 0 0 0
# 0 0 1
# 0 1 1
# """

# def f(n):
#     b = bin(n)[2:]
#     b += b[-1]
#     for i in range(2):
#         b += str(b.count("1") % 2)
#     return int(b, 2)
# for i in range(4, 1000):
#     if f(i) > 97:
#         print(i)
#         break


# d = list(product("ABCDX", repeat=4))
# k = 0
# for i in d:
#     w = ''.join(i)
#     if w.count('X') == 1:
#         k += 1
# print()
#
# def f(s):
#     while "111" in s or "333" in s:
#         if "111" in s:
#             s = s.replace('111', '3', 1)
#         else:
#             s = s.replace('333', '1', 1)
#     return s
#
#
# d = {}
# for i in range(107, 1000):
#     s = '3' * i
#     d[i] = int(f(s))
# dd = sorted(d.items(), key=lambda x: (x[1], x[0]))
# print(dd)

# x = 6 * 512 ** 180 + 7 * 64 ** 181 + 3 * 8 ** 184 + 5 * 8 ** 125 - 65
# k = 0
# while x > 0:
#     if x % 64 == 0:
#         k += 1
#     x //= 64
# print(k)


# @lru_cache(None)
# def f(n):
#     if n <= 2:
#         return n
#     else:
#         return g(n) + f(n - 2)
#
#
# @lru_cache(None)
# def g(n):
#     if n <= 2:
#         return n
#     else:
#         return f(n - 1) - g(n - 2)
#
# print(g(15))

# k = 0
# ma = 0
# with open('17.txt') as f:
#     data = f.read().split('\n')[:-1]
#     d = list(map(int, data))
# m = max([x for x in d if abs(x) % 11 == 0])
# for i in range(len(d) - 1):
#     s1,s2 = d[i], d[i+1]
#     if s1 % 11 == 0 or s2 % 11 == 0:
#         if s1 + s2 <= m:
#             k += 1
#             ma = max(ma, s1 + s2)
# print(k, ma)



# @lru_cache(None)
# def f(start, finish, t1=False, t2=False):
#     if start > finish:
#         return 0
#     if start == 7:
#         t1 = True
#     if start == 16:
#         t2 = True
#     if start == finish and t1 and t2:
#         return 1
#     return f(start + 1, finish, t1, t2) + f(start * 2, finish, t1, t2)
#
#
# print(f(2, 39))

# with open('24.txt') as f:
#     d = f.read().strip()
# i = 0
# m = 0
# s = ''
# while i < len(d):
#     if len(s) < 2:
#         s += d[i]
#     else:
#         if d[i] != "Z":
#             s += d[i]
#         else:
#             if s[-2] == "X" and s[-1] == "Y":
#                 m = max(m, len(s))
#                 s = s[-1] + "Z"
#             else:
#                 s += d[i]
#     i += 1
# print(m)

# def f(n):
#     d = []
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             d.extend([i, n // i])
#     return len(set(d)), sum(set(d))
#
#
# for i in range(135790, 163229):
#     k, s = f(i)
#     if s > 460000:
#         print(i, k, s)

# k = 0
# mi = 1000000000
# with open("26 (4).txt") as f:
#     s = f.readline()
#     m, m1 = int(s.split()[0]), int(s.split()[1])
#     data = f.read().split()
#     d = list(map(int, data))
# d.sort(reverse=True)
# for i in d:
#     if m - i >= 0:
#         m -= i
#         k += 1
#         mi = min(mi, i)
# print(k, mi, m)


with open("27a.txt") as f:
    kolvo = int(f.readline().strip())
    data = f.read().split('\n')[:-1]
    d = []
    for i in data:
        s1, s2 = int(i.split()[0]), int(i.split()[1])
        d.append((min(s1, s2), max(s1, s2)))
d = sorted(d, key=lambda x: (x[0], x[1]), reverse=True)
print(d)
# mi = 67300
# ost = mi % 7 == 2
# ma = 115780
# ost_1 = ma % 7 == 0
for j in d:
    s1 = j[1] - j[0]
    s2 = j[0] % 7 - j[1] % 7
    print(s1, s2)
print(115780 - 1711 - 807)
