from functools import lru_cache

"""def f(n):
    if n< 5: return 5 - n
    if n >= 5 and n % 3 == 0:
        return 4 * (n-5) * f(n-5)
    return 3 * n + 2 * f(n-1) + f(n-2)

print(f(20))"""

"""def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n-1) - 2*g(n-1)
def g(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n-1) + 2*g(n-1)

print(g(21))"""

"""def f(n):
    if n == 0:
        return 1
    return  f(n-1) * n


print(f(100))
# просто факториал"""

"""@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    return (3 * n + 5) * f(n-1)

for i in range(1,2100):
    f(i)
print(f(2073) / f(2070))"""

"""@lru_cache(None)
def f(n):
    if n >= 10_000:
        return n
    if n < 10_000 and n % 2 == 0:
        return 1 + f(n//2)
    return n**2 + f(n + 2)

print(f(192)-f(9))
Ручками считаем
"""

"""def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

# @lru_cache(None)
# def f(n):
#     if n >= 5000:
#         return fact(n)
#     if 1 <= n < 5000:
#         return 2 * f(n+1) / (n + 1)

print(5*6*7*1000/2/2/2)"""

"""@lru_cache(None)
def f(n):
    if n > 30:
        return n * n + 5*n + 4
    if n <= 30 and n % 2 == 0:
        return f(n+1) + 3*f(n+4)
    return 2 * f(n + 2) + f(n+5)

for i in range(30, 1, -1):
    f(i)
k = 0
for i in range(1, 1001):
    d = f(i)
    s = sum([int(x) for x in str(d)])
    if s == 27:
        k +=1
print(k)"""

"""@lru_cache(None)
def f(n):
    if n < 4:
        return 1
    if n > 3 and n % 2 != 0:
        return n
    return f(n-1) + f(n-2) + f(n-3)

for i in range(1, 2255):
    f(i)

print(f(2254) - f(2252))"""

"""print(999+333+111+74+80+86)"""

"""@lru_cache(None)
def f(n):
    if n < - 100000:
        return 1
    if n > 10:
        return f(n - 1) + 3 * f(n - 3) + 2
    return -f(n - 1)


for i in range(-100_000, 20, 1):
    f(i)
print(f(20))"""

"""def f(n, k):
    if k == 0:
        return 0
    if k > 0 and n % k == 0:
        return f(n, k - 1) + k ** 2
    return f(n, k - 1)


kolvo = 0
n = 11223456789
k = 123456789
while k > 0:
    if n % k == 0:
        kolvo += k ** 2
    k -= 1
print(kolvo)"""


"""@lru_cache(None)
def f(n):
    if n == 1:
        return 2
    return f(n - 1) * ((3 ** (n % 5)) / (3 ** (n % 7)))


for i in range(2, 1030):
    f(i)

print((3 ** (1026 % 7) * 3 ** (1027 % 7) * 3 ** (1028 % 7) * 3 ** (1029 % 7) * 3 ** (1030 % 7)) / (
            3 ** (1026 % 5) * 3 ** (1027 % 5) * 3 ** (1028 % 5) * 3 ** (1029 % 5) * 3 ** (1030 % 5)))"""
