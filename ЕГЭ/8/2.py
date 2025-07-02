from itertools import product
words = list(product("ДЖОБС", repeat=6))
k = 0
for i in words:
    w = ''.join(i)
    if w.count("Д") != 1 or w.count("О") != 1 or w.count("С") != 1 or w.count("Ж") > 2:
        k += 1
print(len(words) -k)
