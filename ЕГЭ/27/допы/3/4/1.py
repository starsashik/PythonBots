def spec(n):
   s = abs(n)
   while s != 0:
       if s % 5 == 1:
           return 0
       s //= 5
   return 1

f = open('27-90a.txt')
n, k, d = [int(x) for x in f.readline().split()]
data = [int(x) for x in f]
max_s = -(10**10)
for i in range(n):
   s = 0
   count = 0
   for j in range(i, n):
       s += data[j]
       if data[j] < 0 and spec(data[j]):
           count += 1
       if s % d == 0 and count % k == 0:
           max_s = max(max_s, s)
print(max_s)

def spec(n):
   s = abs(n)
   while s != 0:
       if s % 5 == 1:
           return 0
       s //= 5
   return 1

f = open('27-90b.txt')
n, k, d = [int(x) for x in f.readline().split()]
ost = [[10**10] * d for i in range(k)]
max_s = -(10**10)
s = 0
count = 0
for i in range(n):
   x = int(f.readline())
   if x < 0 and spec(x):
       count += 1
   s += x
   if count % k == 0 and s % d == 0:
       max_s = max(max_s, s)
   ost_s = s % d
   ost_k = count % k
   if ost[ost_k][ost_s] != 10**10:
       max_s = max(max_s, s - ost[ost_k][ost_s])
   ost[ost_k][ost_s] = min(ost[ost_k][ost_s], s)
print(max_s)