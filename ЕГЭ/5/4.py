def f(n):
    b = bin(n)[2:]
    ed = b[1::2].count('1')
    nul = b[::2].count("0")
    return abs(ed - nul)


for i in range(1022, 10000):
    if f(i) == 5:
        print(i)
        break
