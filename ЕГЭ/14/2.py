def transfer(x, q):
    while x > 0:
        if x % q % 2 != 0:
            return 0
        x //= q
    return 1

data = []
x = 3456
for i in range(2, 11):
    if transfer(x, i):
        data.append(i)
print(sum(data))