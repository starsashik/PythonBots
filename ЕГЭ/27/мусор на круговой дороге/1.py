with open('27-A_6097.txt') as f:
    s = list(map(int, f.read().split('\n')[1:-1]))
    n = 102
mi = 100000000000000000000000000
print(s)
for i in range(n//2):
    j = i + n//2
    m = 0
    for d in range(-(n // 2 // 2), n // 2 // 2 + 1):
        m += abs(d) * s[d + i]
        m += abs(d) * s[(d+j) % n]
    mi = min(m, mi)
print(mi)
