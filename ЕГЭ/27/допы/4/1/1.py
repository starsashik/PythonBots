# f = open("27A_6318.txt")
# n,m = list(map(int,f.readline().split()))
# data = [int(x) for x in f]
# max_k = 0
# for i in range(n):
#     k = 0
#     for j in range(n):
#         if abs(i-j) <= m:
#             k += data[j]
#     max_k = max(max_k,k)
# print(max_k)

f = open("27B_6318.txt")
n,m = list(map(int,f.readline().split()))
data = [int(x) for x in f]
max_k = k = sum(data[:2*m +1])
for i in range(m+1, n -m):
    k = k - data[i-1-m] +data[i+m]
    max_k= max(max_k, k)
print(max_k)
