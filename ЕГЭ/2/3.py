from itertools import product


def F(x, y, z, w):
    return (x or y) and (not (y == z)) and (not w)


for x, y, z, w in product([0, 1], repeat=4):
    if F(x, y, z, w):
        print(x, y, z, w)

"""
x y z w
0 1 0 0
1 0 1 0
1 1 0 0

zyxw
"""
