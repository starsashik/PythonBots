from itertools import permutations
from pprint import pprint

chisla = list(permutations("НИЧЬЯ", 5))
d = list(filter(lambda x: x[0] != "Ь", chisla))
pprint(d)
k = 0
for i in d:
    w = ''.join(i)
    if "ЬИЯ" in w:
        k += 1
print(len(d) - k)
