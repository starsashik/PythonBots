from itertools import product
from pprint import pprint

chisla = list(product("АИКЛМЬ", repeat=6))
d = [''.join(i) for i in chisla]
k = 0
for i in range(len(d)):
    g = d[i]
    if g[0] == 'К' and g[-1] == "Ь" and len(set(g)) == 6:
        if d.index(g[::-1]) - i == 26655:
            print(g, i)