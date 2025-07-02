from itertools import product

dd = list(filter(lambda x: (x[0] != "0" and x.count("6") == 1), product("01234567", repeat=5)))
k = 0
chet = '0246'
for i in dd:
    w = ''.join(i)
    ind = w.index("6")
    if ind == 0 and w[ind + 1] in chet:
        k += 1
    elif ind == 4 and w[ind - 1] in chet:
        k += 1
    elif w[ind - 1] in chet and w[ind + 1] in chet:
        k += 1
print(k)
