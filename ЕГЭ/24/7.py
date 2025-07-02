with open("24-173.txt") as f:
    data = f.read().strip()
m = 3
k = 0
i = 3
s = data[:3]
while i < len(data) - 2:
    if data[i] != s[len(s) - 3]:
        s += data[i]
        k = 0
    else:
        s += data[i]
        k += 1
        if k == 3:
            m = max(m, len(s)-1)
            s = s[-3:]
    i += 1
print(len(s), m)