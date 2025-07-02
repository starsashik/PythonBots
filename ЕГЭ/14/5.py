def f(x, q):
    d = []
    while x > 0:
        if x % q not in d:
            d.append(x % q)
        x //= q
    return len(d)
x = 12**34 + 7 *12**26 - 3*12**16 + 2*12**5 + 552
print(f(x, 12))
