"""from itertools import product
words = list(product("ДЖОБС", repeat=6))
k = 0
for i in words:
    w = ''.join(i)
    if w.count("Д") != 1 or w.count("О") != 1 or w.count("С") != 1 or w.count("Ж") > 2:
        k += 1
print(len(words) -k)
"""

from itertools import product
words = list(product("СТРОКА", repeat=5))
words.sort()
for i in range(len(words)):
    s = ''.join(words[i])
    if (s[0] not in "АСТ") and (s.count("О") == 2) and (i + 1) % 2 == 0:
        print(i+1, s)
