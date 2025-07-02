i = 700011
res = []
kolvo = 0
while kolvo < 5:
    if '1' in str(i):
        i += 13
        continue
    if '2' == str(i)[-1] and '4' == str(i)[-4]:
        i += 13
        continue
    if '0' in str(i) and '3' in str(i):
        dd = []
        s = str(i)
        while s.find('0') != -1:
            dd.append(s.find('0'))
            s = s[s.find('0')+1:]
        if any(j - str(i).find('3') for j in dd):
            i += 13
            continue
    res.append(i)
    i+=13
    kolvo += 1
for i in res:
    print(i, sum([int(j) for j in str(i)]), end=" ")