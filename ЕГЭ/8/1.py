import itertools
from pprint import pprint

words = list(itertools.product('СЕРГ', 'СЕРГЙ', 'СЕРГЙ', 'СЕРГЙ', 'СЕРГ'))
k = 0
for i in words:
    w = ''.join(i)
    if "ЙЕ" in w or 'ЕЙ' in w or w.count('Й') > 1:
        k += 1
print(len(words) - k)
