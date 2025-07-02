# 13036359
"""with open('26_6031.txt') as f:
    n = int(f.readline())
    dd = sorted(list(set([int(x) for x in f])),reverse=True)
diff = 6
for i in range(10):
    res = [dd[i]]
    for j in range(i+1, len(dd)):
        if res[-1] - dd[j] >= diff:
            res += [dd[j]]
    print(len(res), res[-1])"""

"""
with open('26-78.txt') as f:
    s = f.readline()
    dd = sorted(filter(lambda x: x[1] >= 1290, [list(map(int, x.split(" "))) for x in f]),
                key=lambda x: (x[0], -x[1] + x[0]))
print(dd[:100])
res = [[996, 1290]]
for i in dd:
    res += [sorted((list(filter(lambda x: x[0] < res[-1][1], dd))), key=lambda x: -x[1])[0]]
    if res[-1][1] >= int(s.split(' ')[2]):
        break
print(len(res), res[0][1] - int(s.split(' ')[1]))"""

"""with open('26_7709.txt') as f:
    k = int(f.readline())
    d = [[False] + [True] * 600 for x in range(k)]

    n = int(f.readline())
    dd = [list(map(int, x.split(' '))) for x in f]
    print(dd)

kolvo = 0
prev = 0
la = 0

for i in dd:
    st, end = i
    for j in range(k):
        if all(d[j][x] for x in range(st, end+1)):
            d[j][st:end + 1] = [False] * (end-st + 1)
            kolvo += 1
            prev = la
            la = j + 1
            break
print(kolvo, prev)"""

"""with open('26_5228.txt') as f:
    n = int(f.readline())
    dd = sorted([int(x) for x in f],reverse=True)
res = [dd[0]]
for i in dd:
    if res[-1] - i >= 8:
        res += [i]
print(len(res), res[-1])"""

"""with open('26_4688.txt') as f:
    n = int(f.readline())
    dd = sorted([list(map(int, x.split())) for x in f],key=lambda x: (x[0],x[1]))
    d = {}
for i in dd:
    if i[0] not in d:
        d[i[0]] = [i[1]]
    else:
        d[i[0]].append(i[1])
d1 = d.copy()
for i,j in d.items():
    if len(j) < 3:
        d1.pop(i)
kolvo = 0
la = 5000
for i,j in d1.items():
    k = 1
    l1 = []
    for g in range(len(j) - 1):
        if j[g+1] - j[g] == 1:
            k += 1
            if k == 3:
                kolvo += 1
                l1 += [j[g+1] - 3]
                k = 1
        elif k == 2 and j[g + 1] - j[g] == 2:
            kolvo += 1
            l1 += [j[g + 1] - 1]
            k = 1
        elif k == 1 and j[g + 1] - j[g] == 2:
            try:
                if j[g+2] - j[g+1] == 1:
                    kolvo += 1
                    l1 += [j[g] + 1]
                    k = 1
            except:
                pass
        else:
            k = 1
    if l1:
        la = min(l1)
print(kolvo, la)
"""

"""with open('26-82.txt') as f:
    n = int(f.readline())
    dd = sorted([list(map(int, x.split())) for x in f], key = lambda x: (x[0],x[1]))
res = []
d = {}
for i in dd:
    if i[0] not in d:
        d[i[0]] = [i[1]]
    else:
        d[i[0]].append(i[1])
for i,j in d.items():
    res += [(i, sum([1 for x in j if x % 2 != 0]))]
print(sorted(res, key=lambda x:-x[1]))"""

"""with open('26_5643.txt') as f:
    n, m = map(int, f.readline().split())
    zam = []
    kor = []
    for i in range(m):
        s = list(map(int, f.readline().split()))
        zam += [s[1]]
        kor += [s[0]]
    for j in range(n - m):
        kor += [int(f.readline())]
dd = []
for j in zam:
    if j in kor:
        dd += [j]
        kor.remove(j)
dd.sort()
for j in range(30):
    if dd[j] % 2 == 0:
        res = [dd[j]]
        for i in dd:
            if - res[-1] + i >= 9 and res[-1] % 2 != i % 2:
                res += [i]
        print(len(res), res[0])"""

"""with open('26_5679.txt', encoding='utf8') as f:
    n, m = list(map(int, f.readline().split()))
    dd = []
    ddd = []
    for i in range(n):
        s = f.readline().split()
        if 'C' not in s[2]:
            dd += [int(s[1])]
        else:
            d = int(s[1]) * (100 - int(s[0]) % 100) / 100
            dd += [d]
            ddd += [d]
dd.sort()
ddd.sort(reverse=True)
d = []
for i in dd:
    if sum(d) + i <= m:
        d += [i]
    else:
        break
print(round(sum(d)))

for j in ddd:
    if sum(d) - d[-1] + j <= m:
        print(round(j))
        break"""

"""with open("26_5988.txt") as f:
    n = int(f.readline())
    dd = sorted([(int(x.split()[0]), x.split()[1]) for x in f],key =lambda x: x[0])
print(dd)
b = [0] * n
for i in range(n-1):
    m = 0
    for j in range(i):
        if dd[i][0] - dd[j][0] >= 7 and dd[i][1] != dd[j][1]:
            m = max(m, b[j])
    b[i] = m + 1
print(b)
"""
