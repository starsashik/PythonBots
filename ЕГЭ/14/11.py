def f(x):
    res = []
    while x > 0:
        res.append(x % 9)
        x //= 9
    return res


dd = []
for x in range(10, 1000):
    d = f(x)
    if 3 in d and len(d) == 3:
        d1 = f(3 * x)
        if len(d1) == 3:
            dd.append(x)
d = (max(dd) + min(dd))
otv = ''
while d > 0:
    otv += str(d%9)
    d //= 9
print(otv[::-1])
