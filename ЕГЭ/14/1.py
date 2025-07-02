def transfer(x, q):
    res = 0
    while x > 0:
        res += x % q
        x //= q
    return res

data = []
x = 1234
for i in range(2, 11):
    n = transfer(x, i)
    data.append((n, i))
print(sorted(data)[-1])