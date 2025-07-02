with open("24_1.txt") as f:
    d = f.read().strip()
m = 0
for i in d.split("Y"):
    if i.count('.') == 0:
        m = max(m, len(i))
    elif i.count('.') <= 5:
        m = max(m, len(i))
    else:
        s = i.split('.')
        for j in range(0, len(s)-4):
            l = 0
            for g in range(5):
                l += len(s[j+g])
            if j != len(s) - 5:
                m = max(m, l+5)
            else:
                m = max(m, l+4)
print(m)

with open("24_adv.txt") as f:
    d = f.read().strip()
s = d[0]
m = 0
i = 1
j = 0
while i < len(d):
    s += d[i]
    if s.count("A") > 3:
        if s.count('R') >= 2:
            m = max(m, len(s)-1)
            i = s.find("A") + j
            j += s.find("A") + 1
            s = ''
        else:
            s = ''
    i +=1
print(m)

with open("24_2.txt") as f:
    d = f.read().strip()
d = d.replace("ZX", "1").replace("ZY", "1").replace('X', ' ').replace("Y", " ").replace("Z", " ")
print(max([len(x) for x in d.split(' ') if x]))
