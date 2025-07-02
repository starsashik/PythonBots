with open('27-B.txt') as f:
    n = int(f.readline())
    d = list(map(int, f.read().split('\n')[:-1]))
kolvo = 0
for i in range(len(d)):
    p = d[i]
    if p % 979801 != 0:
        kolvo += 1
        for j in range(i + 1, len(d)):
            if (p * d[j]) % 979801 != 0:
                p *= d[j]
                kolvo += 1
            else:
                break
print(kolvo)
