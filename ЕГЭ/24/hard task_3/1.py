f = open('24 (1).txt')

s = f.read().strip()

comb = 'ABC, BAC, CAB, CBA'
s = s.replace('ABCAB', 'ABC*CAB')
s = s.replace('ABCBA', 'ABC*CBA')
s = s.replace('BACBA', 'BAC*CBA')
s = s.replace('CABAC', 'CAB*BAC')
s = s.replace('CBABC', 'CBA*ABC')
print(s)
max_len = 2
cur_len = 2
for i in range(len(s)):
    if s[i] == '*':
        for j in range(i + 4, len(s), 4):
            if s[j] == '*':
                cur_len += 1
                max_len = max(max_len, cur_len)
            else:
                cur_len = 2
                break
print(max_len)
