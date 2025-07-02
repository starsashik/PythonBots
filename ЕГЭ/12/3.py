def f(s):
    while '00' not in s:
        s = s.replace('01', '210', 1)
        s = s.replace('02', '3101', 1)
        s = s.replace('03', '2012', 1)
    return s

print()