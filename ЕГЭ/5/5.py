# def f(x):
#     b = str(x)
#     res = []
#     for i in range(len(b) - 1):
#         res.append(int(b[i] + b[i + 1]))
#     return (max(res) - min(res))
# for i in range(100, 10000):
#     if f(i) == 44:
#         print(i)
#         break

# def f(x):
#     sumchet = 0
#     for i in range(len(str(x))):
#         if int(str(x)[i]) % 2 == 0:
#             sumchet += int(str(x)[i])
#     b = str(x)[1::2]
#     c = [int(y) for y in b]
#     sumchetm = sum(c)
#     return abs(sumchetm - sumchet)
# for i in range(2, 10000):
#     if f(i) == 7:
#         print(i)
#         break

# def f(x):
#     x1 = x
#     if x % 2 == 0:
#         x1 //= 2
#     else:
#         x1 -= 1
#     if x1 % 3 == 0:
#         x1 //= 3
#     else:
#         x1 -= 1
#     if x1 % 7 == 0:
#         x1 //= 7
#     else:
#         x1 -= 1
#     return x1
# k = 0
# for i in range(2, 100000):
#     if f(i) == 1:
#         k += 1
# print(k)

# def f(x):
#     b = bin(x)[2:]
#     n = ''
#     if int(b) % 2 == 0:
#         n = '10' + b + '10'
#     else:
#         n = '1' + b + '00'
#     return int(n, 2)
# res = []
# for i in range(1, 10000):
#     if f(i) > 100:
#         res.append(f(i))
# print(min(res))

# def f(x):
#     b = bin(x)[2:]
#     n = ''
#     summa = sum([int(x) for x in b])
#     if summa % 2 == 0:
#         n = '10' + b[2:] + '0'
#     else:
#         n = '11' + b[2:] + '1'
#     return int(n, 2)
# for i in range(1, 1000):
#     if f(i) >= 16:
#         print(i)
#         break

# def f(x):
#     b = bin(x)[2:]
#     n = ''
#     ed = b[1::2].count('1')
#     nul = b[::2].count('0')
#     return abs(ed - nul)
# for i in range(1, 10000):
#     if f(i) == 5:
#         print(i)
#         break

# def f(x):
#     b = bin(x)[2:]
#     n = b[:-1] + b[1] + b[1]
#     return int(n, 2)
# for i in range(2, 1000):
#     if f(i) > 76:
#         print(i)
#         break

# def f(N, M):
#     n = str(N)
#     m = str(M)
#     p1 = 1
#     p2 = 1
#     for i in range(len(n)):
#         if int(n[i]) % 2 == 0 and int(n[i]) != 0:
#             p1 *= int(n[i])
#         if int(n[i]) % 2 == 1:
#             p2 *= int(n[i])
#     for i in range(len(m)):
#         if int(m[i]) % 2 == 0 and int(m[i]) != 0:
#             p1 *= int(m[i])
#         if int(m[i]) % 2 == 1:
#             p2 *= int(m[i])
#     return abs(p1 - p2)
# for i in range(1, 10000):
#     if f(120, i) == 29:
#         print(i)
#         break

# def f(N):
#     n = []
#     nn = ''
#     if N % 2 == 0:
#         for i in range(4):
#             n.append(str(N)[i])
#         n.sort(reverse=True)
#         for i in range(len(n)):
#             nn += str(n[i])
#         nn = int(nn) // 2
#         return nn
#     else:
#         for i in range(4):
#             n.append(str(N)[i])
#         n.sort()
#         for i in range(len(n)):
#             nn += str(n[i])
#         nn = int(nn) * 2
#         return nn
# for i in range(1000, 10000):
#     if f(i) - i == 1:
#         print(f(i))
#         break

def f(n):
    n = str(n)[::-1]
    b = []
    for i in range(0, 16):
        if i % 2 == 1:
            aa = int(n[i]) * 2
            if aa < 10:
                b.append(aa)
            else:
                aa = int(str(aa)[0]) + int(str(aa)[1])
                b.append(aa)
        else:
            b.append(int(n[i]))
    if sum(b) % 10 == 0:
        return b
for i in range(1234_5678_9101_1121, 1_0000_0000_0000_0000):
    if f(i):
        print(str(i)[8:])
        break