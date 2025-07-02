def f(x, q):
    res = ""
    while x > 0:
        res += str(x%q)
        x //= q
    return res[::-1]


for i in range(10000):
    x = 5**2026 + 7*5**1013 + 107 - i
    d = f(x, 6)
    if d.count("5") - d.count("0") == 28:
        print(i)
        break