with open('27_B.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    dd = list(map(int, f.read().split('\n')[:-1]))
ch_26 = 0
ch = 0
ne_26 = 0
ne = 0
d = dd[:k]
ma = 0
for j in range(k, len(dd)):
    if d:
        if d[0] % 26 == 0:
            if d[0] % 2 == 0:
                ch_26 = max(d[0], ch_26)
            else:
                ne_26 = max(ne_26, d[0])
        else:
            if d[0] % 2 == 0:
                ch = max(ch, d[0])
            else:
                ne = max(ne, d[0])
        d.pop(0)
    if dd[j] % 26 == 0:
        if dd[j] % 2 == 0:
            if not d:
                ch_26 = max(dd[j], ch_26)
            ma = max(dd[j] + ne, dd[j] + ne_26, ma)
        else:
            if not d:
                ne_26 = max(ne_26, dd[j])
            ma = max(ma, dd[j] + ch, dd[j] + ch_26)
    else:
        if dd[j] % 2 == 0:
            if not d:
                ch = max(dd[j], ch)
            ma = max(dd[j] + ne_26, ma)
        else:
            if not d:
                ne = max(ne, dd[j])
            ma = max(ma, dd[j] + ch_26)
print(ma)
