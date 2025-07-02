"""data = [int(x) for x in open('17 (1).txt')]
res = []
for i in range(len(data) - 1):
    s1, s2 = data[i], data[i+1]
    if (s1 + s2)%2 == 0 and str(s1 + s2)[-1] != '6':
        res.append((s1 + s2)/2)
print(len(res), max(res))"""

"""with open('17 (2).txt') as f:
    data = list(map(int, f))
res = []
m = max([x for x in data if x % 22 == 0])
for i in range(len(data) - 1):
    s1, s2 = data[i], data[i+1]
    if s1 > m or s2 > m:
        res.append(s1 + s2)
print(len(res), min(res))"""

"""with open('17 (3).txt') as f:
    data = list(map(int, f))
m = min([x for x in data if x % 103 == 0])
res = []
for i in range(len(data) - 1):
    s1, s2 = data[i], data[i+1]
    if (s1 + s2) % 2 == 0 and abs(s1 - s2) % m == 0:
        res.append(s1 + s2)
print(len(res), max(res))"""

"""with open('17 (4).txt') as f:
    data = list(map(int, f))
res = []
for i in range(len(data) - 1):
    s1,s2 =data[i], data[i+1]
    if (s1 % 2 == 0 and s1 %4 == 0 and s2 % 2 != 0 and s2 % 11 == 0) or \
            (s1 % 2 != 0 and s1 % 11 == 0 and s2 % 2 == 0 and s2 % 4 == 0):
        res.append(s1 +s2)
print(len(res), max(res))"""

"""with open('17 (5).txt') as f:
    data = list(map(int, f))
res = []
for i in range(len(data) - 1):
    s1, s2 = data[i], data[i+1]
    if (s1 % 9 == 0 and s2 % 9 != 0 and abs(s2) % 8 == 3) or \
            (s1 % 9 != 0 and abs(s1) % 8 == 3 and s2 % 9 == 0):
        res.append(max(s1, s2))
print(len(res), max(res))"""

"""with open('17 (6).txt') as f:
    data = list(map(int, f))
srar = sum(data) / len(data)
res = []
for i in range(len(data) - 1):
    if (data[i] + data[i+1]) > srar and (len(oct(data[i])[2:]) % 2 != 0 or len(oct(data[i + 1])[2:]) % 2 != 0):
        res.append(data[i] + data[i+1])
print(len(res), min(res))"""

"""with open('17 (7).txt') as f:
    data = list(map(int, f))
res = []
srar = sum(data) / len(data)
for i in range(len(data) - 2):
    s1, s2, s3 = data[i], data[i + 1], data[i + 2]
    if (s1 > srar and s2 > srar) or (s1 > srar and s3 > srar) or \
            (s2 > srar and s3 > srar):
        res.append(s1 + s2 + s3)
print(len(res), max(res))"""

"""with open("17 (8).txt") as f:
    data = list(map(int, f))
res = []
for i in range(len(data) - 2):
    s1, s2, s3 = data[i], data[i + 1], data[i + 2]
    if s2 - s1 > 0 and s3 - s2 > 0:
        res.append(max(s1, s2, s3) - min(s1, s2, s3))
print(len(res), min(res))"""

"""data = list(map(int, open('17 (9).txt')))
res = []
for i in range(len(data) - 1):
    s1, s2 = data[i], data[i + 1]
    if int(s1 ** 0.5) == s1 ** 0.5 and int(s2 ** 0.5) == s2 ** 0.5:
        if int(s1 ** 0.5) % 2 == 0 and int(s2 ** 0.5) % 2 == 0:
            res.append(s1 + s2)
print(max(res), len(res))"""

"""def perevod(ch):
    res = ''
    while ch > 0:
        res += str(ch % 7)
        ch //= 7
    return res[::-1]


data = list(map(int, open("17 (10).txt")))
res = []
m = max([x for x in data if x % 107 == 0])
for i in range(len(data) - 1):
    s1, s2 = data[i], data[i + 1]
    if (s1 > m or s2 > m) and ('36' in perevod(s1) or '36' in perevod(s2)):
        res.append(s1 + s2)
print(len(res), min(res))"""

"""data = list(map(int, open('17 (11).txt')))
res = []
for i in range(len(data) - 3):
    if data[i] % 2 == data[i + 2] % 2 and data[i + 1] % 2 == data[i + 3] % 2 and data[i] % 2 != data[i + 1] % 2:
        res.append(data[i] + data[i + 1] + data[i + 2] + data[i + 3])
print(len(res), max(res))
"""

"""def f(s):
    return sum([int(g) for g in str(s)])


data = list(map(int, open('17 (12).txt')))
res = []
m = sum([f(x) for x in data if x % 50 == 0])
for i in range(len(data) - 2):
    s1, s2, s3 = data[i], data[i + 1], data[i + 2]
    if s1 + s2 + s3 < m:
        if (s1 == f(s2) or s1 == f(s3)) or (s2 == f(s1) or s2 == f(s3)) or \
                (s3 == f(s2) or s3 == f(s1)):
            res.append(s1 + s2 + s3)
print(len(res), max(res))
"""

data = list(map(int, open('17 (13).txt')))
res = []
for i in range(len(data) - 1):
    s1, s2 = data[i], data[i + 1]
    if abs(s1 % 17 - s2 % 17) == s1 % 4 + s2 % 4:
        res.append(s1 + s2)
print(len(res), min(res))
