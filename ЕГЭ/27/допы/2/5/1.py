f = open('27-17a.txt')
n = int(f.readline())
data = [int(x) for x in f]
k = ch = nech = ch13 = nech13 = 0
q = data[:5]
for i in range(5, n):
    if q[0] % 26 == 0:
        ch += 1
        ch13 += 1
    elif q[0] % 13 == 0:
        nech += 1
        nech13 += 1
    elif q[0] % 2 == 0:
        ch += 1
    else:
        nech += 1
    q.pop(0)
    q.append(data[i])
    if q[-1] % 26 == 0:
        k += nech
    elif q[-1] % 13 == 0:
        k += ch
    elif q[-1] % 2 == 0:
        k += nech13
    elif q[-1] % 2 != 0:
        k += ch13
print(k)
