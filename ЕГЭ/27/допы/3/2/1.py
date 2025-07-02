# Переборный алгоритм

f = open('27-72a.txt')
n = int(f.readline())
data = [int(x) for x in f]
k = 0

for i in range(n):
    s = 0
    for j in range(i, n):
        s += data[j]
        if s % 71 == 0:
            k += 1
print(k)

# Эффективное решение

f = open('27-72a.txt')
n = int(f.readline())
ost = [0] * 71
k = 0
s = 0
for i in range(n):
    x = int(f.readline())
    s += x
    if s % 71 == 0:
        k += 1
    k += ost[s % 71]
    ost[s % 71] += 1
print(k)
