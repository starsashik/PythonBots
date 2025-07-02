def f(x, q):
    k = 0
    while x > 0:
        if x % q == 1:
            k += 1
        x //= q
    return k


for i in range(1000, 10000):
    x = 4 ** 2015 + 2 ** i - 2 ** 2015 + 15
    if f(x, 2) == 500:
        print(i, 1000)
        break
