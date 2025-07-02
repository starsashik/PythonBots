f = open('28129_B.txt')
n = int(f.readline())
del7 = [0] * 160
nedel7 = [0] * 160
for i in f.readlines():
    x = int(i)
    d = x % 160
    if x % 7 == 0:
        del7[d] = max(del7[d], x)
    else:
        nedel7[d] = max(nedel7[d], x)

ma = 0
s = 0
for i in range(160 - 1):
    for j in range(i + 1, 160):
        if s < del7[i] + nedel7[j]:
            s = del7[i] + nedel7[j]
            ma = (del7[i], nedel7[j])
        if s < nedel7[i] + del7[j]:
            s = nedel7[i] + del7[j]
            ma = (nedel7[i], del7[j])
        if s < del7[i] + del7[j]:
            s = del7[i] + del7[j]
            ma = (del7[i], del7[j])

print(min(ma), max(ma))
