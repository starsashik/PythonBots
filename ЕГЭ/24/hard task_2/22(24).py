with open('22.txt') as f:
    d = f.read().strip()
    d = d[d.find('F')+1:d.rfind("F")].split('F')
k = m = 0
print(len(d))
i = 0
while i < len(d) - 1:
    k = len(d[i]) + 2
    for j in range(i + 1, len(d)):
        if d[i].count("A") > 2:
            i = j
            break
        if d[j].count("A") <= 2:
            k += len(d[j]) + 1
        else:
            i = j
            break
    m = max(m, k)
    i += 1
print(m)