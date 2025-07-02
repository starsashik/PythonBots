from itertools import product, permutations
from pprint import pprint

chisla = list(permutations("0123456789", 6))
chisla = list(filter(lambda x: x[0] != '0', chisla))
chisla = [''.join(i) for i in chisla]

chisla1 = list(product("0123456789", repeat=4))
chisla1 = list(filter(lambda x: x[0] != '0', chisla1))
chisla1 = [''.join(i) for i in chisla1]

k1 = 0
k2 = 0

for i in chisla:
    flag = True
    for j in range(len(i) - 1):
        if (int(i[j]) + int(i[j+1])) % 2 != 1:
            flag = False
            break
    if flag:
        k1 += 1

for i in chisla1:
    flag = True
    for j in range(len(i) - 1):
        if i[j] == i [j+1]:
            flag = False
            break
    if flag:
        k2 += 1
print(f"1 {k1 - k2}") if k1 > k2 else print(f'2 {k2 - k1}')