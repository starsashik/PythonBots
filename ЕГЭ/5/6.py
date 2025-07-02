"""def f(n):
    num = []
    s = str(n)
    for i in range(len(s) - 1):
        num.append(int(s[i] + s[i + 1]))
    return max(num) - min(num)


for i in range(10, 100000):
    if f(i) == 44:
        print(i)
        break
"""

"""def f(n):
    s = str(n)
    ch_ch = sum([int(x) for x in s if int(x) % 2 == 0])
    ch = sum([int(s[x]) for x in range(1, len(s), 2)])
    return abs(ch_ch - ch)


for i in range(2, 10000):
    if f(i) == 7:
        print(i)
        break
"""

"""def f(n):
    if n % 2 == 0:
        n //= 2
    else:
        n -=1
    if n % 3 == 0:
        n //= 3
    else:
        n -= 1
    if n % 7 == 0:
        n //= 7
    else:
        n -= 1
    return n
k = 0
for i in range(2, 1*7*3*2 + 1):
    if f(i) == 1:
        k += 1
print(k)"""

"""
res = []
def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        s = '10' + b + '10'
    else:
        s = '1' + b + '00'
    return int(s,2)
for i in range(1, 100000):
    if f(i) > 100:
        res.append(f(i))
print(min(res))"""

"""def f(n):
    b = bin(n)[2:]
    g = b.count('1')
    s = '1' + str(g % 2) + b[2:] + str(g % 2)
    return int(s,2)

for i in range(1, 10000):
    if f(i) > 16:
        print(i)
        break"""

"""def f(n):
    b = bin(n)[2:]
    ed = b[1::2].count('1')
    nul = b[::2].count('0')
    return abs(ed - nul)


for i in range(2, 100000):
    if f(i) == 5:
        print(i)
        break
"""

"""def f(n):
    b = bin(n)[2:]
    s = b[:-1] + 2 * b[1]
    return int(s, 2)


for i in range(2, 10000):
    if f(i) > 76:
        print(i, f(i))
        break"""

"""def f(n, m):
    p1 = [int(x) for x in str(n) if x != '0' and int(x) % 2 == 0] + [int(x) for x in str(m) if
                                                                     x != '0' and int(x) % 2 == 0]
    p2 = [int(x) for x in str(n) if int(x) % 2 == 1] + [int(x) for x in str(m) if int(x) % 2 == 1]
    p11 = 1
    for i in p1:
        p11 *= i
    p22 = 1
    for i in p2:
        p22 *= i
    return abs(p11 - p22)


for i in range(1, 100000):
    if f(120, i) == 29:
        print(i)
        break
"""

"""def f(n):
    if n % 2 == 0:
        s = sorted(map(int, list(str(n))), reverse=True)
        s = sum([10 ** (3 - i) * s[i] for i in range(len(s))]) // 2
    else:
        s = sorted(map(int, list(str(n))))
        s = sum([10 ** (3 - i) * s[i] for i in range(len(s))]) * 2
    return s


for i in range(10, 1000000):
    if f(i) - i == 1:
        print(f(i))
        break
"""

"""def f(n):
    s = str(n)[::-1]
    b = []
    for i in range(16):
        if i % 2 == 0:
            b.append(int(s[i]))
        else:
            g = int(s[i]) * 2
            b.append(g // 10 + g % 10)
    if sum(b) % 10 == 0:
        return 1
    return 0

for i in range(1234567891011121, 10 **17):
    if f(i):
        print(str(i)[8:])
        break"""

"""def f(n):
    s = str(n)
    if int(s[0]) % 4 == 0:
        s = '9' + s[1:]
    elif int(s[0]) % 2 == 0:
        s = '3' + s[1:]
    if s[0] == '9' and oct(int(s))[-1] == '4':
        return 1
    return 0

k = 0
for i in range(1000, 10000):
    if f(i):
        k += 1
print(k)"""


def f(n):
    s = ";".join(hex(n)[2:])
    s = [int(x, 16) for x in s.split(';')]
    if n % 2 == 0:
        s.append(15)
    else:
        s.append(0)
    for i in range(2):
        s.append(sum(s) % 16)
    if s.count(min(s)) / s.count(max(s)) == 5.0:
        return 1
    return 0


for i in range(1, 100000):
    if f(i):
        print(i)
        break
