from itertools import permutations

dd = list(permutations("АПЕЛЬСИН", 7))
k = 0
for i in dd:
    f = ''.join(i)
    if "Ь" in f:
        if "Ь" == f[0]:
            k += 1
        elif "Ь" == f[-1]:
            k += 1
        elif 'Ь' in f:
            if f[f.find("Ь") - 1] in "АЕИ" or f[f.find("Ь") + 1] in "АЕИ":
                k += 1
print(len(dd)-k)

# 40320
# 32400