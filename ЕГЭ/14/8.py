def f(x, y):
    s1 = 1 * 21 ** 4 + 2 * 21 ** 3 + y * 21 ** 2 + x * 21 + 9
    s2 = 3 * 21 ** 4 + 6 * 21 ** 3 + y * 21 ** 2 + 9 * 21 + 9
    s = s1 + s2
    if s % 18 == 0:
        return s // 18
    return 0


for x in range(1, 21):
    flag = True
    for y in range(1, 21):
        d = f(x, y)
        if not d:
            flag = False
            break
    if flag:
        print(f(x, 5))
