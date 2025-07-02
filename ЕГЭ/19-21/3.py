"""def f(start, X, win, cur):
    if start == x:
        return win % 2 == cur % 2
    if start > x:
        return 0
    if win == cur:
        return 0

    nex = [f(start + 1, x, win, cur + 1),
           f(start + 2, x, win, cur + 1),
           f(start + 3, x, win, cur + 1),
           f(start + 4, x, win, cur + 1)]

    return any(nex) if win % 2 == (cur + 1) % 2 else all(nex)

# k = 0
# for x in range(5, 26):
#     for s in range(1, 20, 2):
#         if f(0, x, s, 0):
#             k += 1
#             break
# print(k)

for x in range(5, 26):
    for s in range(6, 7):
        if f(0, x, s, 0):
            print(x)
            break
"""

"""def f(n, k, win, cur):
    if (n < 3 and k < 3 and n != 2 and k != 2) or n == 0 or k == 0:
        return win % 2 == cur % 2
    if win == cur:
        return 0

    nex = [f(n - 3, k - 3, win, cur + 1)]

    if n % 2 == 0:
        nex += [f(n // 2, n // 2, win, cur + 1)]
    if k % 2 == 0:
        nex += [f(k // 2, k // 2, win, cur + 1)]

    return any(nex) if win % 2 == (cur + 1) % 2 else all(nex)


for k in range(1, 32):
    if f(20, k, 2, 0) or f(20, k, 4, 0):
        print(k)"""

"""def f(k, s, win, cur):
    if k + s >= 30:
        return win % 2 == cur % 2
    if win == cur:
        return 0

    nex = [f(k + 1, s, win, cur + 1),
           f(k, s + 1, win, cur + 1),
           f(k * 2, s, win, cur + 1),
           f(k, s * 3, win, cur + 1)]

    return any(nex) if win % 2 == (cur + 1) % 2 else all(nex)


# for k in range(1, 29):
#     for s in range(1, 29):
#         if k + s <= 29:
#             if f(k, s, 2, 0):
#                 print((k, s))
#                 break


# for k in range(1, 23):
#     if f(k, 7, 3, 0) and not f(k, 7, 1, 0):
#         print(k)

# for s in range(1, 29):
#     if f(1, s, 4, 0):
#         print(s)"""


def f(s, win, cur):
    if s >= 51:
        return win % 2 == cur % 2
    if win == cur:
        return 0

    nex = []

    if s + 1 <= 60:
        nex += [f(s + 1, win, cur + 1)]
    if s + 2 <= 60:
        nex += [f(s + 2, win, cur + 1)]
    if s * 2 <= 60:
        nex += [f(s * 2, win, cur + 1)]

    return any(nex) if win % 2 == (cur + 1) % 2 else all(nex)


for s in range(1, 51):
    for i in range(1, 7):
        if f(s, i, 0):
            print(s, i)
            break
