# def f(s):
#     while '10' in s:
#         if '10' in s:
#             s = s.replace('10', '001', 1)
#         if '1' in s:
#             s = s.replace('1', '01', 1)
#     return len(s)
#
#
# def simple(x):
#     for i in range(2, int(x**0.5) + 1):
#         if x % i == 0:
#             return 0
#     return 1
#
# k = 0
# for i in range(10,100):
#     s = '1' + i*'0'
#     if simple(f(s)):
#         k += 1
# print(k)

# def f(s):
#     while '10' in s or '1' in s:
#         if '10' in s:
#             s = s.replace('10', '001', 1)
#         elif '1' in s:
#             s = s.replace('1', '0', 1)
#     return len(s)
#
#
# for i in range(1, 10000):
#     s = '1' + i*'0'
#     if 100 <= f(s) < 1000:
#         print(i)
#         break


# def f(s):
#     while '>1' in s or '>2' in s or '>0' in s:
#         if '>1' in s:
#             s = s.replace('>1', '20>', 1)
#         if ">2" in s:
#             s = s.replace('>2', "00>", 1)
#         if ">0" in s:
#             s = s.replace(">0", "10>", 1)
#
# """
# из 1 -- 2
# из 2 -- 0
# из 0 -- 1
# сумма = 599
# k - 0
# m - 1
# n - 2
# n = 0
# 599 - 200m = 199k
# """

# def f(s):
#     while '111' in s or '333' in s:
#         if '111' in s:
#             s = s.replace('111' ,'3', 1)
#         else:
#             s = s.replace('333', '1', 1)
#     return int(s)
#
# d = {}
# for i in range(101, 1000):
#     s = '3' * i
#     d[i] = f(s)
#
# print(sorted(d.items(), key=lambda x: (x[1], x[0])))


# def f(s):
#     while '555' in s or '888' in s:
#         s = s.replace('555', '8', 1)
#         s = s.replace('888', '55', 1)
#     return s
#
# d = []
#
# for i in range(3, 100):
#     s = '5' * i
#     d.append(f(s))
# print(len(set(d)))


# def f(s):
#     while '555' in s or '888' in s:
#         s = s.replace('555', '8', 1)
#         s = s.replace('888', '55', 1)
#     return s.count("8")
#
# for i in range(101, 1000):
#     s = '5' * i
#     if not f(s):
#         print(i)
#         break


# def f(s):
#     while '42' in s or '32' in s:
#         if '42' in s:
#             s = s.replace('42', '51', 1)
#         else:
#             s = s.replace('32', '61', 1)
#     d = 0
#     for i in range(1, 7):
#         d += i * s.count(str(i))
#     return d
#
# s = '32' * 15 +'42' * 5 + '4' * 5
# print(f(s))


# def f(s):
#     while '12' in s or '13' in s:
#         s = s.replace('12', '21', 1)
#         s = s.replace("31", '23', 1)
#         s = s.replace('13', '23', 1)
#     return 2 * s.count('2') + 3 * s.count("3")
# """
# Получается так что за каждую 1 мы получаем одну 2 и за каждую 3 мы получаем 3
# 404-3-3= 398 => 199 единиц и 2 тройки
# """
# print(201)


# def f(s):
#     while '01' in s or '02' in s or '03' in s:
#         s = s.replace('01', '30', 1)
#         s = s.replace('02', '3103', 1)
#         s = s.replace('03', '1201', 1)
#     return s
#
# """
# получаем что за "1" x мы получаем одну 3
# за "2" y получаем две 1, две 3 и одну 2
# за "3" z получаем по одной всего
# нам надо 42-1, 31-2, 59-3
# 42 = 2y +z
# 31 =y + z
# 59 =x +2y +z
# получаем что y = 11
# """


# for i in range(1, 10000):
#     s = 15 * 4 + 16 * 4 + 5 * i
#     d = 15 * 2 + 16 * 2 + 6 * i + 1
#     if s % d == 0:
#         print(i)
#         break


# def f(s):
#     while '10' in s or '1' in s:
#         if '10' in s:
#             s = s.replace('10', '0001', 1)
#         elif '1' in s:
#             s = s.replace('1', '0', 1)
#     return len(s)
#
# k = 0
# for i in range(1, 101):
#     s = '1' + '0' *i
#     if f(s) % 7 == 0:
#         k += 1
# print(k)


# def f(s):
#     while '21' in s or '31' in s or '32' in s:
#         if '21' in s:
#             s = s.replace('21', '12', 1)
#         if "31" in s:
#             s = s.replace('31', '13', 1)
#         if '32' in s:
#             s = s.replace('32', '23', 1)
#     return s[49]
#
#
# for i in range(17, 1000):
#     s = '321' * i
#     if f(s) == '2':
#         print(3*i)
#         break