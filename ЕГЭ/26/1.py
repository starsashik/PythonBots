with open("26-73.txt") as f:
    n = int(f.readline())
    d = {}
    for i in f.readlines():
        s = i.split(" ")
        row = int(s[0])
        col = int(s[1])
        if row in d:
            d[row].add(col)
        else:
            d[row] = set()
            d[row].add(col)
dd = sorted(d.items())
dd = list(filter(lambda x: len(x[1]) > 1, dd))
max_k = 1
max_row = 1
for i in dd:
    k = 1
    pl = sorted(i[1])
    for j in range(len(pl) - 1):
        if pl[j+1] - pl[j] == 1:
            k += 1
            if k >= max_k:
                max_k = k
                max_row = i[0]
        else:
            k = 1
print(max_k, max_row)