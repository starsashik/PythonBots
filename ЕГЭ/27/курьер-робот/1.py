with open('123.txt') as f:
    n = int(f.readline())
    nums = [int(f.readline()) for _ in range(n)]

pr = [0] * (n+1)
for i in range(n):
    pr[i+1] = pr[i] + nums[i]
print(pr)

left_s = 0
mx = right_s = sum(nums[i] * i for i in range(n))
print(mx)

for i in range(1, n):
    # right_s -= (pr[-1] - pr[i])
    right_s -= sum([nums[x] for x in range(i, n)])
    # left_s += pr[i]
    left_s += sum([nums[x] for x in range(0, i)])
    mx = max(mx, right_s + left_s)
print(mx)