with open("26 (2).txt") as f:
    n = f.readline()
    n = 982000
    d = sorted(list(f.read().split("\n")), key=lambda x: int(x.split()[0]))
k = 0
s = 0


# находим сумму
def ss(l):
    sq = 0
    for i in l:
        sq += int(i.split()[0])
    return sq


a = []
b = []

dd = []
# Ищем максимальное число товаров которое можем купить
for i in d:
    if s + int(i.split()[0]) <= n:
        k += 1
        s += int(i.split()[0])
# Распределяем товары по а и б
for i in d:
    a.append(i) if i.split()[1] == "A" else b.append(i)

# забиваем нужное количество товаров товарами б
for j in range(k):
    dd.append(b[j])

kolvo = 0
for i in range(len(dd) - 1, 1, -1):
    for j in range(len(a)):
        if a[j] != 0:
            if int(a[j].split()[0]) < int(dd[i].split()[0]):
                dd[i] = a[j]
                a[j] = 0
                kolvo += 1
                break
            elif ss(dd) - int(dd[i].split()[0]) + int(a[j].split()[0]) <= n:
                dd[i] = a[j]
                a[j] = 0
                kolvo += 1
                break
print(kolvo, n - ss(dd))
