from itertools import permutations


def f(s):
    while '00' not in s:
        s = s.replace('012', '30', 1)
        if '011' in s:
            s = s.replace('011', '20', 1)
            s = s.replace('022', '40', 1)
        else:
            s = s.replace('01', '10', 1)
            s = s.replace('02', '101', 1)
    return (s.count('1'), s.count('2'), s.count('3'))


res = []
for i in range(1, 1048575):
    s = bin(i)[2:].zfill(20)
    if s.count('0') != s.count('1'):
        continue
    s = s.replace('0', '2')
    s1 = '0' + s + '0'
    x, y, z = f(s1)
    if x == 7 and y == 5:
        res.append(z)
print(min(res))
