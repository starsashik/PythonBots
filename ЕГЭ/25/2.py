def f(n):
    divs = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.append(i)
            divs.append(n//i)
    return sum(divs)
res = []
kolvo = 0
i = 10**7
while kolvo< 5:
    s = str(i)
    if s[0] == '9' and len(s) >= 5 and s[-1] == '7' and '55' in s:
        res.append(i)
        kolvo +=1
    i -=1
for i in range(len(res)-1, -1,-1):
    print(res[i], f(res[i])%21,end=' ')