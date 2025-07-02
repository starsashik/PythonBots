f = open("24-39621.txt")
k = 0
glas = 'AEIOUY'
sogl = 'BCDFGHJKLMNPQRSTVWXZ'
d = f.read().strip().split('AB')[1:-1]
for i in d:
    if len(i) > 300:
        g = s = 0
        for j in i:
            if j in glas:
                g +=1
            elif j in sogl:
                s += 1
        if g <= s:
            k += 1
print(len(d))
print(k)
