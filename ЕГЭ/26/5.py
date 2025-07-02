with open("26 (1).txt") as f:
    n = int(f.readline())
    d = sorted(list(map(int, f.read().split())), reverse=True)
k = 0
dd = []
current = 10003
for i in d:
    if current - i >= 3:
        dd.append(i)
        current = i
        k += 1
print(k, min(dd))