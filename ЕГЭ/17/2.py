with open("17_1.txt") as f:
    f.readline()
    d = list(map(int, f.read().split()))
m = max([i for i in d if str(i)[-1] == '3']) ** 2
k = 0
mm = -20000000000
for i in range(len(d) - 1):
    s1 = d[i]
    s2 = d[i + 1]
    if (str(s1)[-1] == '3' and str(s2)[-1] != '3') or (str(s2)[-1] == '3' and str(s1)[-1] != '3'):
        if s1**2 + s2**2 >= m:
            k += 1
            mm = max(mm, s1**2 + s2**2)
print(k, mm)
