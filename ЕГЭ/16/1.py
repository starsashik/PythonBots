"""def f(n):
    if n == 0:
        return 5
    if n > 0 and n % 2 == 0:
        return 1 + f(n // 2)
    return f(n // 2)


for i in range(1, 35):
    if f(i) == 7:
        print(i, f(i), bin(i)[2:])
"""

print(bin(1_000_000_000)[2:])


def f(n):
    if n == 0:
        return 0
    if n % 2 != 0:
        return f(n - 1) + 1
    return f(n // 2)

"111011100110101100101000000000"
'111000000000000000000000000000'
"469762048"
"939524096"
kolvo = 3654
"""for i in range(2,29):
    kolvo += (i * (i-1))//2"""

for i in range(469762048, 939524096 + 1):
    if bin(i)[2:].count('1'):
        kolvo += 1
print(kolvo)