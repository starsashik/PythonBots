from itertools import product

d = list(product("КРЕМНИЙ", repeat=5))
k = 0
for i in d:
    w = "".join(i)
    if (w.count("Е") + w.count("И")) % 2 != 0 or w.count("Й") > 2 or (w.count("Е") + + w.count("И")) == 0:
        k += 1
print(len(d) - k)
