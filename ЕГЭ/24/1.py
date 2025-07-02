with open("task24-1.txt", encoding='utf8') as f:
    dd = {}
    k = 1
    data = f.read().strip()
for i in range(len(data) - 1):
    if data[i] == data[i+1]:
        k += 1
        if data[i] not in dd:
            dd[data[i]] = k
        else:
            dd[data[i]] = max(k, dd[data[i]])
    else:
        k = 1
print(sorted(dd.items(), key=lambda x:(-x[1], x[0])))
g = open('task24-1.txt')
if 'B'*6 in g.read():
    print(1)