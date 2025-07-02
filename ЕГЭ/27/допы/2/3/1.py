# Выбираем максимальное число в каждой тройке и ищем минимальную нечетную разность между максимальным числом тройки и остальными числами. Если четность двух групп s1 и s2 оказалась равна, вычитаем минимальную разность из группы с максимальной суммой.

f = open('27-B (2).txt')
n = int(f.readline())
max_s = 0
min_diff = 10 ** 20
s1 = s2 = 0
for i in f:
    x, y, z = sorted([int(k) for k in i.split()])
    max_s += z
    s1 += x
    s2 += y
    if (z - y) % 2 != 0:
        min_diff = min(min_diff, z - y)
    if (z - x) % 2 != 0:
        min_diff = min(min_diff, z - x)
if s1 % 2 == s2 % 2:
    print(max_s - min_diff)
else:
    print(max_s)
