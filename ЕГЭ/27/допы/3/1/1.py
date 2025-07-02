# Переборный алгоритм

f = open('27-73a.txt')
n = int(f.readline())
data = [int(x) for x in f]
max_s = 0
for i in range(n):
    s = 0
    for j in range(i, n):
        s += data[j]
        if s % 93 == 0 and s % 2 != 0:
            max_s = max(max_s, s)
print(max_s)

# Эффективное решение

f = open('27-73b.txt')
n = int(f.readline())
ost_sum_chet = [0] * 93
ost_sum_nechet = [0] * 93
max_s = 0
s_93 = 0
for i in range(n):
    x = int(f.readline())
    s_93 += x
    d = s_93 % 93
    if d == 0 and s_93 % 2 != 0:
        max_s = max(max_s, s_93)
    elif s_93 % 2 == 0:
        if ost_sum_nechet[d] != 0:
            max_s = max(max_s, s_93 - ost_sum_nechet[d])
    elif d != 0 and s_93 % 2 != 0:
        if ost_sum_chet[d] != 0:
            max_s = max(max_s, s_93 - ost_sum_chet[d])
    if s_93 % 2 == 0 and ost_sum_chet[d] == 0:
        ost_sum_chet[d] = s_93
    elif s_93 % 2 != 0 and ost_sum_nechet[d] == 0:
        ost_sum_nechet[d] = s_93

print(max_s)
