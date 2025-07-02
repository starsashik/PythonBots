def f(x, q):
    res = ""
    while x > 0:
        if x % q == 10:
            res += "A"
        elif x % q == 11:
            res += "B"
        elif x % q == 12:
            res += "C"
        elif x % q == 13:
            res += "D"
        elif x % q == 14:
            res += "E"
        else:
            res += str(x % q)
        x //= q
    return res[::-1]


x = 3 * 15 ** 1140 + 2 * 15 ** 1015 + 15 ** 923 - 3 * 15 ** 85 + 2 * 15 ** 74 + 3
d = f(x, 15)
print(d)
k = 1
m = 2
current = ""
for i in range(len(d) - 1):
    if d[i] == d[i + 1] == current:
        k += 1
    else:
        current = d[i + 1]
        k = 1
        m = max(k, m)
    m = max(m, k)
print(m)
