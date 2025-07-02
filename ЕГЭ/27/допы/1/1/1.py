# полный перебор
with open('27989_A.txt') as f:
    n = int(f.readline())
    dd = list(map(int, f.read().split('\n')))
k = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if dd[i] * dd[j] % 26 == 0:
            k += 1
print(k)

#Эффективный способ (считаем количество чисел, которые делятся на 26, на 13, на 2, не делятся ни на что из перечисленного, комбинаторно считаем количество пар)
with open('27989_B.txt') as f:
    n = int(f.readline())
    k26 = 0
    k13 = 0
    k2 = 0
    k = 0
    for i in f.readlines():
        if int(i) % 26 == 0:
            k26 += 1
        elif int(i) % 13 == 0:
            k13 += 1
        elif int(i) % 2 == 0:
            k2 += 1
        else:
            k += 1
res = k2 * k13 + k26 * (k + k2 + k13) + k26 * (k26 - 1) // 2
print(res)

#Если бы в этой задаче нам нужно было вывести максимальное произведение подходящей пары:

f = open('27989_B.txt')
n = int(f.readline())
k26 = [0,0]
k13 = 0
k2 = 0
k = 0
for i in f.readlines():
   if int(i) % 26 == 0 and int(i) > max(k26):
       k26 = [max(k26), int(i)]
   elif int(i) % 13 == 0 and int(i) > k13:
       k13 = int(i)
   elif int(i) % 2 == 0 and int(i) > k2:
       k2 = int(i)
   elif int(i) > k:
       k = int(i)
res = max(k26[0] * k26[1], k13 * k2, max(k26) * k, max(k26) * k2, max(k26) * k13)
print(res)