with open("27886.txt") as f:
    n = f.readline()
    n = 5955
    d = sorted(list(map(int, f.read().split())))
print(d)
k = 0
dd = []
for i in d:
    if sum(dd) + i <= n:
        dd.append(i)
        k += 1
s = sum(dd)
for j in range(len(d) - 1, len(dd), -1):
    if sum(dd) < sum(dd) - dd[-1] + d[j] <= n:
        dd[-1] = d[j]
        break
print(sum(dd), k, max(dd))