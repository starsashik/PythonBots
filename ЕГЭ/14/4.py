def f(x, q):
    f1 = 9 * q ** 4 + 7 * q ** 3 + 5 * q ** 2 + 9 * q + x
    f2 = 3 * q ** 4 + x * q ** 3 + 1 * q ** 2 + 8
    if (f1 + f2) % 11 == 0:
        return (f1+f2) // 11
    return 0


for i in range(0, 17):
    res = f(i, 17)
    if res:
        print(res)
        break