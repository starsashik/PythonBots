"""def f(ch):
    s1 = int(str(ch)[0]) + int(str(ch)[1])
    s2 = int(str(ch)[1]) + int(str(ch)[2])
    s3 = str(min(s1, s2)) + str(max(s1, s2))
    return int(s3)


k = 0
for i in range(100, 1000):
    if f(i) == 1216:
        k += 1
print(k)
"""

"""def f(n):
    s = bin(n)[2:]
    if n % 2 == 0:
        s = '1' + s + '0'
    else:
        s = '11' + s + '11'
    return int(s, 2)


for i in range(1, 1000):
    if f(i) > 52:
        print(i)
        break"""


"""def f(n):
    s = bin(n)[2:]
    for i in range(2):
        s += str(s.count('1') % 2)
    return int(s, 2)


d = []
for i in range(1, 1000):
    if f(i) < 90:
        d.append(f(i))
    else:
        break
print(max(set(d)))"""


"""
def f(n):
    s = bin(n)[2:].rjust(8, '0')
    s = s.replace('1', '*')
    s = s.replace('0', '1')
    s = s.replace('*', "0")
    return int(s, 2) - n


for i in range(0, 256):
    if f(i) == 133:
        print(i)
        break
"""