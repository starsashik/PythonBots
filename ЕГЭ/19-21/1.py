"""def f(start, cur, win):
    if 20 <= start <= 30:
        return win % 2 == cur % 2
    if start > 30:
        return win % 2 != cur % 2
    if win == cur:
        return 0
    next_s = [f(start + 1, cur + 1, win),
              f(start * 2, cur + 1, win)]
    return any(next_s) if win % 2 == (cur + 1) % 2 else all(next_s)


for i in range(1, 20):
    for s in range(1, 6):
        if f(i, 0, s):
            print(i, s)
            break
"""

"""def f(start, cur, win):
    if 43 <= start <= 72:
        return win % 2 == cur % 2
    if start > 72:
        return win % 2 != cur % 2
    if win == cur:
        return 0
    next_s = [f(start + 1, cur + 1, win),
              f(start * 2, cur + 1, win),
              f(start * 3, cur + 1, win)]
    return any(next_s) if win % 2 == (cur + 1) % 2 else all(next_s)


for i in range(1, 43):
    for s in range(1, 6):
        if f(i, 0, s):
            print(i, s)
            break
"""

"""def f(start, cur, win, h=0):
    if start >= 43:
        return win % 2 == cur % 2
    if win == cur:
        return 0
    next_s = []
    if h != 1:
        next_s.append(f(start + 1, cur + 1, win, h=1))
    if h != 2:
        next_s.append(f(start + 2, cur + 1, win, h=2))
    if h != 3:
        next_s.append(f(start * 2, cur + 1, win, h=3))
    return any(next_s) if win % 2 == (cur + 1) % 2 else all(next_s)


for i in range(1, 43):
    for s in range(1, 6):
        if f(i, 0, s):
            print(i, s)
            break"""

"""def f(start, cur, win):
    if start >= 26:
        return win % 2 == cur % 2
    if win == cur:
        return 0
    next_s = [f(start + 1, cur + 1, win),
              f(start + 2, cur + 1, win)]
    if start % 2 != 0:
        next_s.append(f(start * 2, cur + 1, win))
    return any(next_s) if win % 2 == (cur + 1) % 2 else all(next_s)


for i in range(1, 26):
    for s in range(1, 6):
        if f(i, 0, s):
            print(i, s)
            break"""


"""def f(start, cur, win, h2=0, h1=0):
    if start >= 29:
        return win % 2 == cur % 2
    if win == cur:
        return 0
    next_s = []
    if h2 != 1:
        next_s.append(f(start + 1, cur + 1, win, h2=h1, h1=1))
    if h2 != 2:
        next_s.append(f(start + 2, cur + 1, win, h2=h1, h1=2))
    if h2 != 3:
        next_s.append(f(start * 2, cur + 1, win, h2=h1, h1=3))
    return any(next_s) if win % 2 == (cur + 1) % 2 else all(next_s)


for i in range(1, 29):
    for s in range(1, 6):
        if f(i, 0, s):
            print(i, s)
            break"""
