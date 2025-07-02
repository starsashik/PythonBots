with open("24-171.txt") as f:
    data = [x.strip() for x in f.readlines()]
m = 0
kalitka = 'XYZ'
for i in data:
    s = ''
    for j in i:
        if j in kalitka:
            if len(s) > 0:
                if s[-1] == kalitka[kalitka.find(j) - 1]:
                    s += j
                else:
                    m = max(m, len(s))
                    s = j
            else:
                s += j
        else:
            m = max(m, len(s))
            s = ''
    m = max(m, len(s))
print(m)
