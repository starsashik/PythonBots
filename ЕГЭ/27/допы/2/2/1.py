# Для каждого числа находим остаток от его деления на 120. В массив складываем максимальные числа с соответствующим остатком.

f = open('28131_A.txt')
n = int(f.readline())
ost = [0] * 120
para = ""
max_s = 0
for i in f:
    x = int(i)
    d = x % 120
    dd = (120 - d) % 120
    if x + ost[dd] > max_s and x < ost[dd] != 0:
        max_s = x + ost[dd]
        para = (x, ost[dd])
    ost[d] = max(ost[d], x)
print(para)
