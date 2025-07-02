"""def f(first, second, cur, win):
    if first + second > 60:
        return win % 2 == cur % 2
    if cur == win:
        return 0
    if first >= 0:
        next_s = [f(first, second + 1, cur + 1, win),
                  f(first, second + 2, cur + 1, win),
                  f(first, second * 2, cur + 1, win)]
    else:
        next_s = [f(first + 1, second, cur + 1, win),
                  f(first + 2, second, cur + 1, win),
                  f(first * 2, second, cur + 1, win)]
    return any(next_s) if win % 2 == (cur + 1) % 2 else all(next_s)


for i in range(1, 53):
    for s in range(1, 6):
        if f(i, 8, 0, s):
            print(i, s)
            break"""

"""def f(start, cur, win):
    if start >= 82:
        return cur % 2 == win % 2
    if cur == win:
        return 0
    next_s = [f(start + 10, cur + 1, win),
              f(start * 2, cur + 1, win)]
    return all(next_s) if win % 2 == (cur + 1) % 2 else any(next_s)


for i in range(1, 82):
    for s in range(1, 6):
        if f(i, 0, s):
            print(i, s)
            break
"""

"""def f(start, cur, win):
    if start >= 151:
        return win % 2 == cur % 2
    if cur == win:
        return 0
    next_s = []
    if (start + 1) % 3 != 0:
        next_s.append(f(start + 1, cur + 1, win))
    if (start + 2) % 3 != 0:
        next_s.append(f(start + 2, cur + 1, win))
    if (start * 2) % 3 != 0:
        next_s.append(f(start * 2, cur + 1, win))
    return any(next_s) if win % 2 == (cur + 1) % 2 else all(next_s)


for i in range(1, 149):
    if i % 3 != 0:
        for s in range(1, 6):
            if f(i, 0, s):
                print(i, s)
                break
"""

"""def f(start, win, cur, s1=False):
    if start >= 20:
        return win % 2 == cur % 2
    if win == cur:
        return 0
    if not s1:
        next_s = [f(start * 2, win, cur + 1, s1),
                  f(start + 2, win, cur + 1, s1),
                  f(start, win, cur + 1, s1=True)]
    else:
        next_s = [f(start * 2, win, cur + 1, s1),
                  f(start + 2, win, cur + 1, s1)]
    return any(next_s) if win % 2 == (cur + 1) % 2 else all(next_s)


for i in range(1, 20):
    for s in range(1, 12):
        if f(i, s, 0):
            print(i, s)
            break"""


"""def f(start, win, cur):
    if 125 <= start <= 163:
        return cur % 2 == win % 2
    if start > 163:
        return (cur + 1) % 2 == win % 2
    if win == cur:
        return 0
    next_s = [f(start + 2, win, cur + 1),
              f(start + 4, win, cur + 1),
              f(start * 2, win, cur + 1)]
    return any(next_s) if (cur + 1) % 2 == win % 2 else all(next_s)


for i in range(1, 125):
    for s in range(1, 6):
        if f(i, s, 0):
            print(i, s)
            break"""
