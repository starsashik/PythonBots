with open('26-j6.txt') as f:
    n = int(f.readline())
    dd = sorted(list(map(int, f.read().split('\n')[:-1])))
ma = sum(dd) * 0.9
j = 1
while sum(dd) > ma:
    dd[-j] = dd[-j] * 0.8
    j += 1
print(dd)
print(sum(dd)-79.2 + 99 - 76 + 76*0.8,ma)
print(n - j + 1)
