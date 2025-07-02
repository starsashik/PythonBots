def f(x, q):
    res = ""
    while x > 0:
        res += str(x % q)
        x //= q
    return res[::-1]


for x in range(1, 10):
    i = 3 * 7 ** (x + 1) + 13 * 7 ** (x + 2) + 31 * 7 ** (3 * x) + 1 * 7 ** (2 * x)
    d = f(i, 7)
    if sum(list(map(int, list(d)))) == 18:
        print(x)
        break
