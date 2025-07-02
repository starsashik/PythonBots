from itertools import product
def f(x,y,z,w):
    return ((not y) <= (z == w)) and ((z <= x) == w)

print('x y z w')
for x,y,z,w in product([0,1], repeat=4):
    if f(x,y,z,w):
        print(x,y,z,w)
"""
x y z w
0 1 0 1
1 0 1 1
1 1 0 1
"""