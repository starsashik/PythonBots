with open("24-164.txt") as f:
    data = [x for x in f.readlines() if x.count("E") < 20]
m = 1
for i in data:
    for s in range(ord("A"), ord("A") + 27):
        s = chr(s)
        if s in i:
            n = i.rfind(s) - i.find(s)
            m = max(m, n)
print(m)