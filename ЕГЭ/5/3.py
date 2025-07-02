def f(n):
    num = []
    s = str(n)
    for i in range(len(s) - 1):
        ch = s[i] + s[i + 1]
        num.append(int(ch))
    return max(num) - min(num)


for i in range(10, 100000):
    if f(i) == 26:
        print(i)
        break