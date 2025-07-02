# f = open("27A_6320.txt")
# n,m  = list(map(int, f.readline().split()))
# data = [int(x) for x in f]
# max_k = 0
# for i in range(n):
#     k = 0
#     for j in range(n):
#         if min(abs(i-j), n - abs(i-j)) <= m:
#             k += data[j]
#     max_k = max(max_k,k)
# print(max_k)

f = open("27B_6320.txt")
n,m  = list(map(int, f.readline().split()))
data = [int(x) for x in f]
data = data + data
max_k = k = sum(data[:2*m+1])
for i in range(m + 1, 2*n-m):
    k = k- data[i-m-1] + data[i+m]
    max_k = max(max_k,k)

print(max_k)