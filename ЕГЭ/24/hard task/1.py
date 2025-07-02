with open("24-174.txt") as f:
    data = [x for x in f.readlines() if x.count('R') <30]
k = m = 0
for i in data:
    for s in range(ord("A"), ord("A") + 27):
        s = chr(s)
        if s in i:
            n = i.split(s)
            n = n[1:-1]
            # if n[0] != s:
            #     n = n[1:]
            # if n[-1] != s:
            #     n = n[:-1]
            n = [len(x) for x in n if x]
            k += len(n)
            m = max(m, max(n) + 2)
print(m,k)