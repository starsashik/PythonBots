def f(n):
    s = bin(n)[2:]
    ed = s[1::2].count('1')
    no = s[::2].count('0')
    return abs(ed - no)


for i in range(10000000000000):
    if f(i) == 5:
        print(i)
        break
