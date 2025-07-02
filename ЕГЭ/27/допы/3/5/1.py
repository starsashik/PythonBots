f = open('27_A.txt')
n = int(f.readline())
data = [int(x) for x in f]
max_s = 0
min_len = 10**10
for i in range(n):
   s = 0
   curr_len = 0
   for j in range(i, n):
       s += data[j]
       curr_len += 1
       if s % 43 == 0:
           if max_s < s:
               max_s = s
               min_len = curr_len
           elif max_s == s:
               min_len = min(min_len, curr_len)
print(min_len)


f = open('27_B.txt')
n = int(f.readline())
mins = {0: (0, 0)}
res = []
s = 0
for i in range(1, n + 1):
   x = int(f.readline())
   s += x
   if s % 43 in mins:
       res.append((s - mins[s % 43][0], i - mins[s % 43][1]))
   else:
       mins[s % 43] = (s, i)
print(sorted(res, key=lambda x: (x[0], -x[1]))[-1])
