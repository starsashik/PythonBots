f = open('27-93a.txt')
n, k = [int(x) for x in f.readline().split()]
data = [int(x) for x in f]
max_s = 0
for i in range(n):
    s = 0
    curr_k = 0
    for j in range(i, n):
        if data[j] < 0 and str(data[j])[-1] == '3':
            curr_k += 1
        s += data[j]
        if curr_k == k:
            max_s = max(max_s, s)
print(max_s)

f = open('27-93b.txt')
n, k = [int(x) for x in f.readline().split()]
data = [10 ** 10] * n
max_s = 0
s = 0
curr_k = 0
for i in range(n):
    x = int(f.readline())
    s += x
    if x < 0 and str(x)[-1] == '3':
        curr_k += 1
    if curr_k == k:
        max_s = max(s, max_s)
    elif curr_k > k:
        max_s = max(max_s, s - data[curr_k - k])
    data[curr_k] = min(data[curr_k], s)
print(max_s)
