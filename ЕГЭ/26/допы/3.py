with open('26_6641.txt') as f:
    n, ma = list(map(int, f.readline().split(' ')))
    dd = f.read().split('\n')[:-1]
W = []
S = []
for i in dd:
    if i.split(' ')[1] == 'W':
        W += [int(i.split(' ')[0])]
    else:
        S += [int(i.split(' ')[0])]
W.sort()
S.sort()

dd = [int(x.split(' ')[0]) for x in dd]
dd.sort()
kolvo = 0
s = 0
for i in dd:
    if s + i <= ma:
        s += i
        kolvo += 1
print(kolvo)

dd = []
s = 0
for i in S:
    if s + i <= ma:
        s += i
        dd += [i]
kolvo1 = len(dd)

j = 1
while len(dd) != kolvo:
    if ma - sum(dd) >= W[0]:
        dd += [W.pop(0)]
        j += 1
    else:
        dd[-j] = W.pop(0)
        j += 1
        kolvo1 -= 1
print(kolvo1, ma - sum(dd))
