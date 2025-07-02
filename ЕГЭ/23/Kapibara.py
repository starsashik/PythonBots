import csv
from functools import lru_cache

"""
4183
4837
4949
5074
5088
"""


def f1(start, finish):
    if start < finish:
        return 0
    if start == finish:
        return 1
    n = f1(start - 8, finish) + f1(start // 2, finish)
    return n


print("Задание 4183", f1(102, 43) * f1(43, 5))


def f2(start, finish):
    if start > finish:
        return 0
    if start == 21:
        return 0
    if start == finish:
        return 1
    if start % 2 == 0:
        n = f2(start + 1, finish) + f2(start + 4, finish) + f2(start + start + 2, finish)
    else:
        n = f2(start + 1, finish) + f2(start + 4, finish) + f2(start + start + 1, finish)
    return n


print("Задание 4837", f2(2, 11) * f2(11, 26))


def f3(start, finish, op=''):
    if start > finish: return 0
    if start == finish: return 1
    if not op:
        n = f3(start + 1, finish) + f3(start + 2, finish, "+2") + f3(start * 2, finish)
    else:
        n = f3(start + 1, finish) + f3(start * 2, finish)
    return n


print("Задание 4949", f3(1, 12))


@lru_cache(maxsize=128, typed=False)
def f4(start, finish, num_11=False, op=''):
    if start > finish: return 0
    if start == 11: num_11 = True
    if start == 23: return 0
    if start == finish and num_11: return 1
    if not op:
        n = f4(start + 1, finish, num_11, "+1") + f4(start + 2, finish, num_11) + f4(start * 2, finish, num_11)
    else:
        n = f4(start + 2, finish, num_11) + f4(start * 2, finish, num_11)
    return n


print("Задание 5074", f4(3, 79))


def f5(start, finish):
    if start < finish: return 0
    if start == finish: return 1
    if int(start ** 0.5) == start ** 0.5:
        n = f5(start - 3, finish) + f5(start - 4, finish) + f5(int(start ** 0.5), finish)
    else:
        n = f5(start - 3, finish) + f5(start - 4, finish)
    return n


print("Задание 5088", f5(36, 21) * f5(21, 3))


@lru_cache(None)
def f6(start, finish, num_15=False, op=''):
    if start > finish: return 0
    if start == 15: num_15 = True
    if start == 25 or start == 30: return 0
    if start == finish and num_15: return 1
    if not op:
        n = f6(start + 1, finish, num_15) + f6(start + 2, finish, num_15) + f6(start * 3, finish, num_15, '*3')
    else:
        n = f6(start + 1, finish, num_15) + f6(start + 2, finish, num_15)
    return n


print(f6(1, 43))


@lru_cache(None)
def f7(start, finish):
    if start > finish: return 0
    if '3' in str(start): return 0
    if start == finish: return 1
    n = f7(start + 1, finish) + f7(start * 2, finish)
    return n


print(f7(1, 40))

with open("22 (3).csv") as f:
    r = list(csv.reader(f, delimiter=","))[1:]
final_time = {}
data = {}
for i in r:
    id_pr = int(i[0])
    time_pr = int(i[1])
    depends = [int(x) if x else "" for x in i[2].split(';')]
    if depends == ['']:
        final_time[id_pr] = time_pr
    else:
        data[id_pr] = (time_pr + 3, depends)
while data:
    keys = list(data.keys())
    for i in keys:
        time_pr, depends = data[i]
        if all((x in final_time) for x in depends):
            max_time = max([final_time[x] for x in depends])
            final_time[i] = time_pr + max_time
            del data[i]
print(max(final_time.values()))
