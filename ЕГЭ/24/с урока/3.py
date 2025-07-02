with open('24_1077.txt') as f:
    s = f.read().strip()
ma = 0
cur = 1
i = 0
s = s.replace('A', " ")
s = s.replace("B", " ")
s = s.replace("C", " ")
for i in s.split(' '):
    cur = 1
    g = i + "0"
    for j in range(len(g) - 1):
        if int(g[j]) - int(g[j+ 1]) >= 0:
            cur += 1
            ma = max(ma,cur)
        else:
            cur = 1
print(ma)