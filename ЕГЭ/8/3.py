from itertools import product

d = list(product("ABCD", repeat=4))
k = 0
for i in d:
    flag = True
    for j in range(len(i) - 1):
        if ord(i[j+1]) - ord(i[j]) > 0:
            flag = False
            break
    if not flag:
        k += 1
print(len(d) - k)