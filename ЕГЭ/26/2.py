with open("26-48.txt") as f:
    n = f.readline()
    d = list(map(int, f.read().split()))
k = 0
dd = []
for i in range(len(d) - 1):
    for j in range(i, len(d)):
        s1 = d[i]
        s2 = d[j]
        if s1 != s2:
            sr = (s1 + s2) / 2
            dd.append(sr)
ddd = []
for h in dd:
    for g in sorted(d):
        if abs(g - h) == 5:
            print(1)
            ddd.append(h)
print(min(ddd))