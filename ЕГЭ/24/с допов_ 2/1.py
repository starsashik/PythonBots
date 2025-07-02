"""f = open('24_1143.txt').read()
k = 0
for i in range(len(f)):
    if f[i] == 'A':
        for j in range(6, 10):
            if i + j < len(f) and f[i + j] == 'F':
                k += 1
print(k)"""

"""with open('24_887.txt') as f:
    s = f.read().strip()
d = {}
for i in range(len(s) - 1):
    if s[i] == 'X':
        d[s[i+1]] = d.get(s[i+1], 0) + 1
print(sorted(d.items(), key = lambda x: (-x[1], x[0])))"""

"""with open('24_1147.txt') as f:
    s = f.read().strip()
d = {}
for i in range(len(s) - 2):
    if s[i + 1] == s[i + 2]:
        d[s[i]] = d.get(s[i], 0) + 1
print(sorted(d.items(), key=lambda x: (-x[1], x[0])))"""

"""with open('24_1148.txt') as f:
    s = f.read().split('\n')[:-1]
d = {}
for i in range(len(s)):
    d[i] = s[i].count('Q')
g = sorted(d.items(), key=lambda x: (-x[1]))
print(g)
s = s[835]
dd = {}
for i in s:
    dd[i] = dd.get(i, 0) + 1
print(sorted(dd.items(), key = lambda x: (x[1], x[0])))
r = open('24_1148.txt').read()
print(r.count('C'))"""

"""with open('24_1064.txt') as f:
    s = f.read().split('\n')
g = ''
for i in s:
    kolvo = 1
    ma = 1
    ss = ''
    for j in range(len(i) - 1):
        if i[j] == i[j+1]:
            kolvo += 1
        else:
            if kolvo > ma:
                ss = i[j]
                ma = kolvo
            elif kolvo == ma:
                if i[j] not in ss:
                    ss += i[j]
            kolvo = 1
    g += ss
d = {}
for i in g:
    d[i] = d.get(i, 0) + 1
print(sorted(d.items(), key=lambda x: -x[1]))"""

# Домашка

"""with open('24_1144.txt') as f:
    s = f.read().strip()
ma = 10**6
for i in range(len(s)):
    if s[i] == "A":
        d = len(s[i:(s[i:]).find("F")]) + 1
        if d > 2:
            ma = min(ma, d)
print(ma)"""

"""with open('24_1149.txt') as f:
    s = f.read().strip()
d = {}
for i in range(len(s) - 2):
    if s[i] == 'A' and s[i+2] == 'C':
        d[s[i+1]] = d.get(s[i+1], 0) + 1
print(sorted(d.items(), key=lambda x: (-x[1], x[0])))"""

"""with open("24_1255.txt") as f:
    s = f.read().split('\n')[:-1]
ma = 0
for i in s:
    if i.count('A') < 25:
        for g in range(ord('A'), ord("Z") + 1):
            ma = max(ma, i.rfind(chr(g)) - i.find(chr(g)))

print(ma)"""

"""with open("24_2150.txt") as f:
    s = f.read().strip()
d = {}
for i in range(len(s) - 4):
    if s[i] == "C" and s[i+1] == 'A' and s[i+2] not in "ABF" and s[i+3] == 'A' and s[i+4] == 'C':
        d[s[i+2]] = d.get(s[i+2], 0) + 1
print(sorted(d.items(), key= lambda x: (-x[1])))
print("E101")"""

"""with open("24_2684.txt") as f:
    s = f.read().strip()
d = {}
for i in range(ord("A"), ord("Z") + 1):
    d[chr(i)] = s.count(chr(i))
print(sorted(d.items(), key=lambda x: (-x[1], x[0])))"""

"""with open("24_2509.txt") as f:
    s = f.read().strip()
d={}
for i in range(ord("A"), ord("Z") + 1):
    d[chr(i)] = s.count(chr(i))
print(sorted(d.items(), key = lambda x: (-x[1])))
print(38820 - 37934)"""

"""with open("24_2508.txt") as f:
    s = f.read().split('\n')[:-1]
ma = 0
r = 0
for i in range(len(s)):
    if s[i].count("Q") >= ma:
        r = i
        ma = s[i].count("Q")
d = s[r]
dd = {}
for j in range(ord("A"), ord("Z") + 1):
    dd[chr(j)] = d.count(chr(j))
g = sorted(dd.items(), key=lambda x: x[1])[0][0]
f = open("24_2508.txt").read()
print(g, f.count(g))"""

"""with open("24_2507.txt") as f:
    s = f.read().split("\n")[:-1]
d = {}
for i in range(len(s)):
    ma = 1
    cur = ''
    kolvo = 1
    for j in range(len(s[i]) - 1):
        if s[i][j] == s[i][j + 1]:
            kolvo += 1
            if kolvo > ma:
                ma = kolvo
                cur = s[i][j]
        else:
            kolvo = 1
    d[i] = [ma, cur]
print(sorted(d.items(), key = lambda x:(-x[1][0], x[0]))[0])
g = s[161]
dd = {}
for i in g:
    dd[i] = dd.get(i, 0) + 1
print(sorted(dd.items(), key=lambda x: (-x[1], x[0])))
r = open("24_2507.txt").read()
print(r.count('K'))"""


"""with open("24_2715.txt") as f:
    s = f.read().strip()
d = {}
for i in range(ord("A"), ord("Z") + 1):
    d[chr(i)] = s.count(chr(i))
print(sorted(d.items(), key=lambda x: (-x[1])))
ma = 'DEV'
mi = 'FIN'

kolvo = 0
for i in range(1, len(s) - 1):
    if s[i] in ma and (s[i-1] in mi or s[i+1] in mi):
        kolvo += 1
if s[0] in ma and s[1] in mi:
    kolvo += 1
if s[-1] in ma and s[-2] in mi:
    kolvo += 1
print(kolvo)"""

f = open('24_1761.txt').read().strip()
max_len = 0
for i in range(1, len(f) - 1):
    cur_len = 0
    for j in range(i - 1, -1, -1):
        if i - j > 0 and i + i - j < len(f) and f[j] == f[i + i - j]:
            cur_len += 1
            max_len = max(max_len, cur_len)
        else:
            break
print(max_len*2 + 1)
max_len = 0
for i in range(1, len(f) - 1):
    if f[i] == f[i + 1]:
        cur_len = 1
        for j in range(i - 1, -1, -1):
            if i - j > 0 and i + i + 1 - j< len(f) and f[j] == f[i + i + 1 - j]:
                cur_len += 1
                max_len = max(max_len, cur_len)
            else:
                break
print(max_len*2)