with open('../../../Äëÿ Èëþõè_2/27.txt') as f:
    n, V, m = list(map(int, f.readline().split(' ')))
    d = sorted([list(map(int, x.split(' '))) for x in f], key=lambda x: x[0])
g = 100083 + 5
data = [0] * g
data_1 = [0] * g
print(d)
for i in d:
    data[i[0]] = i[1] // V if i[1] % V == 0 else i[1] // V + 1
    data_1[i[0]] = i[1]
s = sum(data[:2 * m + 1])
s1 = sum(data_1[:2 * m + 1])
ms = 0
ms1 = 0
if data[m] != 0:
    ms = s
    ms1 = s1
for i in range(m + 1, g - m):
    s = s + data[i + m] - data[i - 1 - m]
    s1 = s1 + data_1[i + m] - data_1[i - 1 - m]
    if data[i] != 0:
        if s1 > ms1:
            ms = s
            ms1 = s1
        elif s1 == ms1:
            ms = max(ms, s)
print(ms)
#4721