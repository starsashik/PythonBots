f = open('26_8482.txt')
n = int(f.readline())
d = [0] * int(f.readline())
time_end = 23 * 60
kolvo = 0
nomer = 0
dd = sorted([list(map(int, x.split(' '))) for x in f], key=lambda x: (x[0], x[1]))
for j in dd:
    start, end = j
    flag = False
    for i in range(len(d)):
        if start > d[i]:
            kolvo += 1
            nomer = i + 1
            d[i] = end + 5
            flag = True
            break
    if not flag:
        min_time = min(d)
        if min_time < start + 10:
            wait_time = min_time - start + 1
            if end + wait_time <= time_end:
                ind = d.index(min_time)
                d[ind] = end + wait_time + 5
                kolvo += 1
                nomer = ind + 1
print(kolvo, nomer)
