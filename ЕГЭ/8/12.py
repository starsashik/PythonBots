from itertools import *

d = set(list(permutations("росомаха",8)))
glas = 'ао'
sogl='рсмх'
k = 0
for i in d:
    w = ''.join(i)
    for j in range(len(w) - 1):
        if (w[j] in glas and w[j+1] in glas) or (w[j] in sogl and w[j+1] in sogl):
            k += 1
            break
print(len(d) - k)