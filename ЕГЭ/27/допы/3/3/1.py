# Переборный алгоритм

f = open('27-A.txt')
n = int(f.readline())
data = [int(x) for x in f]
max_s = 0
for i in range(n):
    k, s = 0, 0
    for j in range(i, n):
        if data[j] % 2 != 0:
            k += 1
        s += data[j]
        if k % 10 == 0:
            max_s = max(max_s, s)
print(max_s)

# Эффективное решение

f = open('27-B.txt')
n = int(f.readline())
ost = [0] * 10
max_s = 0
k, s = 0, 0
for i in range(n):
    x = int(f.readline())
    s += x
    if x % 2 != 0:
        k += 1
    if k % 10 == 0:
        max_s = max(max_s, s)
    else:
        if ost[k % 10] != 0:
            max_s = max(max_s, s - ost[k % 10])
        else:
            ost[k % 10] = s
print(max_s)
