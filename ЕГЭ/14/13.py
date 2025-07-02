def f(ch):
    otv = ''
    while ch > 0:
        otv += str(ch%7)
        ch //= 7
    return otv[::-1]

x = 5 * 343**8 + 4 *49 ** 12 + 7**14 - 98

d = f(x)
for i in range(7):
    print(i, d.count(str(i)))