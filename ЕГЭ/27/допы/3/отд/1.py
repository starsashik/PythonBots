f = open('1.txt')
n, d, t = list(map(int, f.readline().split()))
dd = [0] * n
count = 0
k = 0
for i in range(n):
    j = int(f.readline())
    if j % d == 0:
        k += 1
    else:
        if k >= t:
            count += dd[k-t]
        dd[k] += 1
print(count)