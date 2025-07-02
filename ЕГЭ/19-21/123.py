"""def f(start, win_step, curr_step):
    if start >= 68:
        return win_step % 2 == curr_step % 2
    if win_step == curr_step:
        return 0
    next_step = [f(start+1, win_step, curr_step + 1),
                 f(start+4, win_step, curr_step + 1),
                 f(start*5, win_step, curr_step + 1)]
    return any(next_step) if (curr_step + 1) % 2 == win_step % 2 else all(next_step)


for s in range(1,68):
    for step in range(1,6):
        if f(s, step, 0):
            print(s, step)
            break


def ff(start, second, win_step, curr_step):
    if start + second >= 77:
        return win_step % 2 == curr_step % 2
    if win_step == curr_step:
        return 0
    next_step = [ff(start + 1, second, win_step, curr_step + 1),
                 ff(start * 2, second, win_step, curr_step + 1),
                 ff(start, second + 1, win_step, curr_step + 1),
                 ff(start, second * 2, win_step, curr_step + 1)]
    return any(next_step) if (curr_step + 1) % 2 == win_step % 2 else all(next_step)


for s in range(1, 70):
    for step in range(1, 6):
        if ff(s, 7, step, 0):
            print(s, step)
            break
"""

"""def f(first, second, win_step, curr_step):
    if first + second >= 61:
        return win_step % 2 == curr_step % 2
    if win_step == curr_step:
        return 0
    next_step = [f(first + 1, second, win_step, curr_step+1),
                 f(first*4, second,win_step, curr_step + 1),
                 f (first, second+ 1, win_step,curr_step+ 1),
                 f(first, second*4, win_step, curr_step+1)]
    return any(next_step) if (curr_step+1) % 2 == win_step % 2 else all(next_step)


for i in range(1, 57):
    for step in range(1, 6):
        if f(3, i, step, 0):
            print(i, step)
            break
"""

"""def f(first, second, win_step, curr_step):
    if first + second >= 41:
        return win_step % 2 == curr_step % 2
    if win_step == curr_step:
        return 0
    next_step = [f(first + 1, second + 2, win_step, curr_step+1),
                 f(first+ 2, second + 1,win_step, curr_step + 1),
                 f (first, second*2, win_step,curr_step+ 1),
                 f(first*2, second, win_step, curr_step+1)]
    return any(next_step) if (curr_step+1) % 2 == win_step % 2 else all(next_step)


for i in range(1, 33):
    for step in range(1, 6):
        if f(8, i, step, 0):
            print(i, step)
            break
"""
"""def f(first, second, win_step, curr_step):
    if first + second >= 69:
        return win_step % 2 == curr_step % 2
    if win_step == curr_step:
        return 0
    next_step = [f(first + 1, second, win_step, curr_step+1),
                 f(first, second + 1,win_step, curr_step + 1),
                 f (first*2, second, win_step,curr_step+ 1),
                 f(first, second*3, win_step, curr_step+1)]
    return any(next_step) if (curr_step+1) % 2 == win_step % 2 else all(next_step)


for i in range(1, 59):
    for step in range(1, 6):
        if f(10, i, step, 0):
            print(i, step)
            break"""


"""def f(s, d, win, cur):
    if s + d <= 40:
        return win % 2 == cur % 2
    if win == cur:
        return 0
    next_s = [f(s - 1, d, win, cur + 1),
              f(s, d - 1, win, cur + 1), ]
    if s % 2 == 0:
        next_s.append(f(s // 2, d, win, cur + 1))
    else:
        next_s.append(f(s // 2 + 1, d, win, cur + 1))
    if d % 2 == 0:
        next_s.append(f(s, d // 2, win, cur + 1))
    else:
        next_s.append(f(s, d // 2 + 1, win, cur + 1))
    return any(next_s) if win % 2 == (cur + 1) % 2 else all(next_s)


for s in range(21, 200):
    for i in range(1, 6):
        if f(20, s, i, 0):
            print(s, i)
            break
"""