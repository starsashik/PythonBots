razn = 9
zam = []
dlin_kor = []
res = []
with open('26.txt') as f:
    inf = list(map(int, f.readline().split()))
    dd = f.readlines()
    for i in range(len(dd)):
        if i < 3250:
            s1, s2 = map(int, dd[i].split('\t'))
            zam.append(s2)
            dlin_kor.append(s1)
        else:
            dlin_kor.append(int(dd[i]))
zam = set(zam)
dlin_kor = list(set(dlin_kor))
dlin_kor.sort(reverse=True)

dlin = dlin_kor.copy()
for i in dlin_kor:
    if i not in zam:
        dlin.remove(i)

print(dlin)

res.append(dlin.pop(1))

for box in dlin:
    if res[-1] - box >= razn and box % 2 != res[-1] % 2 and box in zam:
        res.append(box)
if res[-1] % 2 != 0:
    res.pop(-1)
print(len(res))
print(res[-1])

