with open('27_B_7627.txt') as f:
    k = int(f.readline())
    n = int(f.readline())
    dd = [int(x) for x in f]
ma = 0
back = 0
for x in range(k, n):
    back = max(back, dd[x - k])
    ma = max(ma, back + dd[x])
print(ma)
