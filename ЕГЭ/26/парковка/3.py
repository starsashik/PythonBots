with open('26.txt') as f:
    n = int(f.readline())
    d = []
    for i in f:
        x, y, z = int(i.split(' ')[0]), int(i.split(' ')[1]), i.split(' ')[2].strip()
        d += [(x, x + y, z)]
ka = [0] * 70
kb = [0] * 30
d = sorted(d, key=lambda x: (x[0]))
kolvo = 0
nom = 0
for x in d:
    flag = True
    if x[2] == 'A':
        for i in range(len(ka)):
            if ka[i] <= x[0]:
                ka[i] = x[1]
                flag = False
                break
        if flag:
            for i in range(len(kb)):
                if kb[i] <= x[0]:
                    kb[i] = x[1]
                    flag = False
                    break
    else:
        for i in range(len(kb)):
            if kb[i] <= x[0]:
                kb[i] = x[1]
                kolvo += 1
                flag= False
                break
    if flag:
        nom += 1
print(kolvo, nom)