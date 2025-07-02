f = open('27_B_7275.txt')
n, m = list(map(int, f.readline().split(' ')))
data = [0] * 10_000_000
for i in f:
    km, k = list(map(int, i.split(' ')))
    kont = k // 30 if k % 30 == 0 else k // 30 + 1
    data[km] = kont

max_s = s = sum(data[:2 * m + 1])
for i in range(m + 1, 10_000_000-m):
    s = s + data[i + m] - data[i - 1 - m]
    if data[i] != 0:
        max_s = max(max_s, s)
print(max_s)