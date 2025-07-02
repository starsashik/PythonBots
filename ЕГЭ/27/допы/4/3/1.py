# f = open('27_A_6760.txt')
# n = int(f.readline())
# data = []
# for i in range(n):
#     km, k = [int(x) for x in f.readline().split()]
#     kont = k // 48 if k % 48 == 0 else k //48 + 1
#     data += [(km, kont)]
#
# min_s = 10 ** 10
# for i in range(n):
#     s = 0
#     for j in range(n):
#         len_road = abs(data[i][0] - data[j][0])
#         s += len_road *data[j][1]
#     min_s = min(min_s,s)
# print(min_s)

f = open('27_B_6760.txt')
n = int(f.readline())
data = [0] * 10_000_000
for i in range(n):
    km, k = [int(x) for x in f.readline().split()]
    kont = k // 48 if k % 48 == 0 else k //48 + 1
    data[km] = kont

min_s = 10 ** 20
s = 0
sm = sum(data)
for i in range(10_000_000):
    s += i *data[i]
prev = data[0]
for i in range(1, 10_000_000):
    s = s+ prev - (sm - prev)
    if data[i]:
        min_s = min(min_s, s)
    prev += data[i]
print(min_s)