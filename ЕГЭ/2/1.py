from itertools import product

print("x y z w")
for x, y, z, w in product([0, 1], repeat=4):
    f = ((y <= w) == (x <= (not z))) and (x or w)
    if not f:
        print(x, y, z, w, 0)
    else:
        print(x,y,z,w,1)
"""
x y z w
0 0 0 1 1
0 0 1 1 1
1 0 0 0 1
1 0 0 1 1

1 0 1 1 0
0 1 0 1 1
"""
