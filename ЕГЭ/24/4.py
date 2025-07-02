f = open("24-1(1).txt")
d = f.read().strip()
data = []
s = d[0]
i = 0
while i < len(d) - 1:
    if d[i] + d[i+1] != "BC" and d[i] + d[i+1] != "CB":
        s += d[i+1]
    else:
        if s.count("E") > s.count("A"):
            data.append(s)
        s = d[i+1]
    i +=1
if s.count("E") > s.count("A"):
    data.append(s)
print(len(sorted(data, key=lambda x: len(x), reverse=True)[0]))