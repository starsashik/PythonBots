from itertools import permutations

chisla = set(permutations("ШАРЛАТАН", 8))
k = 0
for i in chisla:
    w = ''.join(i)
    flag = False
    for j in range(len(i) - 1):
        if i[j] != "А" and i[j + 1] != "А" or i[j] == "А" and i[j + 1] == "А":
            flag = True
    if flag:
        k += 1
print(k)
