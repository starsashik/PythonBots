"""with open('24 (1).txt') as f:
    s = f.read().strip()
d = 'DBAC'
n = 1
while d in s:
    n += 1
    d = 'DBAC' * n
n -= 1
print(n)

print(("DBAC" * n + "D") in s)
print(("DBAC" * n + "DB") in s)
print(("DBAC" * n + "DBA") in s)"""

"""with open('24 (2).txt') as f:
    s = f.read().strip()

ma = 0
cur = 1
i = 0
while i < len(s) - 1:
    if s[i] <= s[i+1]:
        cur += 1
        ma = max(ma,cur)
    else:
        cur = 1
    i += 1
print(ma, cur)"""

"""with open('24 (3).txt') as f:
    s = f.read().strip()
s = s.replace('AA', "*")
s = s.replace("CC", "*")
for i in "ABC":
    s = s.replace(i, " ")
print(max([len(x) for x in s.split(' ')]))"""

"""with open('24 (4).txt') as f:
    s = f.read().strip()
d = 'CA'
n = 1
while d in s:
    n += 1
    d = 'CA' * n
n -= 1
print(n)
print(("CA" * n + "C") in s)"""

"""with open('24 (5).txt') as f:
    s = f.read().strip()

ma = 0
cur = 2
i = 0
while i < len(s) - 2:
    if s[i] == s[i + 2] and s[i] != s[i + 1]:
        cur += 1
        ma = max(ma, cur)
    else:
        cur = 2
    i += 1
print(ma)
"""

"""with open('24 (6).txt') as f:
    s = f.read().strip()
ma = 0
cur = ''
i = 0
while i < len(s):
    if s[i] == '0' and (len(cur) == 0 or cur[-1] == '0'):
        cur += s[i]
    elif s[i] == '1' and cur and (cur[-1] in '01'):
        cur += s[i]
    else:
        ma = max(ma, len(cur))
        cur = ''
    i += 1
print(ma, len(cur))"""

"""with open('24 (7).txt') as f:
    s = f.read().strip()
ma = 0
cur = 0
for i in range(3):
    while i < len(s) - 2:
        if s[i] == 'X' and s[i + 2] == 'Y' or s[i] == 'Z' and s[i + 2] == 'Y':
            cur += 1
            ma = max(ma, cur)
        else:
            cur = 0
        i += 3
print(ma)"""

"""with open('24 (8).txt') as f:
    s = f.read().strip()
    ps = {"AB", 'CB', 'BC', 'BA'}
    mc = c = 0
    for i in range(len(s)):
        if s[i:i+2] in ps:
            c += 1
            mc = max(mc, c)
        else:
            c = 0
    print(mc)
"""

"""with open('24 (9).txt') as f:
    s = f.read().strip()
ma = 0
d = 'AEIOUY'
for j in d:
    s = s.replace(j, "*")
i = 0
for i in s.split('.'):
    if i.count('*') <= 7:
        ma = max(ma, len(i))
    else:
        ii = i.split('*')
        for j in range(len(ii) - 7):
            k = 7
            for g in range(8):
                k += len(ii[j+g])
            ma = max(ma, k)
print(ma)
"""
"""from itertools import product

dd = product("ABCDEF", repeat=3)

ps = [''.join(x) * 2 for x in dd]
with open('24 (10).txt') as f:
    s = f.read().strip()
ma = 0
cur = 0

i = 0
while i < len(s):
    if s[i:i + 6] in ps:
        ma = max(ma, cur + 5)
        cur = 0
    else:
        cur += 1
        ma = max(ma, cur)
    i += 1
print(ma)"""