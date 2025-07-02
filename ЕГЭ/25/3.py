def f(n):
    divs = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.extend([i, n//i])
    return sum(divs)
i = 16606
res = []
kolvo = 0
while kolvo<7:
    s = str(i)
    if s[-1] == '6' and s.count('6') >= 3 and len(s) >= 5 and s[1] == '6':
        if i % 6 == 0 and i % 7 == 0 and i % 8 == 0:
            res.append(i)
            kolvo += 1
    i += 10
for i in res:
    print(i, f(i),end=' ')
"""56616 162240 66696 191040 161616 527744 166656 523264 266616 862680 360696 1094400 366576 1083264"""
"""56616 162240 66696 191040 161616 527744 166656 523264 266616 862680 360696 1094400 366576 1083264 """