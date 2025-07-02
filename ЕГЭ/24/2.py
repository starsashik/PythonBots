f = open("24-39619.txt")
d = f.read().strip()
data = []
s = d[0]
for i in range(len(d) - 1):
    if d[i] < d[i+1]:
        s += d[i+1]
    else:
        data.append(s)
        s = d[i+1]
print(data)
for i in data:
    if len(i) == 6:
        print(i)
        break
