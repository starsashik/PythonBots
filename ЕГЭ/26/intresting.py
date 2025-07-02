with open("26.txt") as f:
    n = f.readline()
    d = sorted(list(map(int, f.read().split())))
s = 0
k = 0
dd = []
for i in d:
    if 210 <= i <= 220:
        s += i
        k += 1
    else:
        dd.append(i)

d = []
i = 0

for j in dd:
    if s + sum(d) + j <= 10000:
        k += 1
        d.append(j)
        i += 1

g = len(dd) - 1

while g >= 0:
    if sum(d) - d[i - 1] + dd[g] <= 10000 - s:
        d[i - 1] = dd[g]
        i -= 1
        g -= 1
    else:
        g -= 1
s += sum(d)
print(k, s)
