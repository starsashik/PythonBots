def f(n):
    b = bin(n)[2:]
    b = b.replace('0', '*')
    b = b.replace('1', '0')
    b = b.replace('*', '1')
    return n - int(b, 2)


for i in range(1, 10900):
    if f(i) == 999:
        print(i)
        break
