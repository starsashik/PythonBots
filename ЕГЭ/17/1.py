with open("17 (3).txt", encoding='utf8') as f:
    d = list(map(int, f.readlines()))
    k = 0
    maxa = 0

for i in range(len(d) - 1):
    for j in range(i + 1, len(d)):
        if (d[i] + d[j]) % 126 == 0:
            k += 1
            maxa = max(maxa, d[i] + d[j])
print(k, maxa)
