f = open('27-A (1).txt')
n = int(f.readline())
max_s = 0
min_diff = [10 ** 20, 10 ** 20]
count_ch = count_nech = 0
for i in f:
    x, y = sorted([int(z) for z in i.split()])
    max_s += y
    if y % 2 == 0:
        count_ch += 1
    else:
        count_nech += 1
    if (y - x) % 2 != 0:
        if y - x < min(min_diff):
            min_diff.pop()
            min_diff.insert(0, y - x)
        elif y - x < max(min_diff):
            min_diff[-1] = y - x
# если больше одной то просто вычитаем наименьшую разность, если 1 то сразу два числа надо изменить
print(count_ch, count_nech)
print(max_s % 2)
print(max_s - sum(min_diff))
print(max_s - min(min_diff))
