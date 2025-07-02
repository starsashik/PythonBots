def f(x, y, q1, q2):
    s1 = x * q1 ** 4 + 2 * q1 ** 3 + 3 * q1 ** 2 + x * q1 + 5
    s2 = 6 * q2 ** 4 + 7 * q2 ** 3 + y * q2 ** 2 + 9 * q2 + y
    s = s1 - s2
    if s % 57 == 0:
        return s // 57
    return 0


for x in range(1, 22):
    for y in range(1, 13):
        d = f(x, y, 22, 13)
        if d:
            print(x, y, x+y, d)
