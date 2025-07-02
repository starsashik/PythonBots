#5381
with open('24_5381.txt') as f:
    s = f.read().strip()

sogl = 'BCDF'
glass = 'AEU'

ma = 0
last = 0
queue = []
for i in range(len(s) - 2):
    if s[i] in sogl and s[i+1] in glass and s[i+2] in sogl:
        ma = max(ma,i - last + 2)
        if len(queue) > 1:
            last = queue.pop(0)
        queue += [i + 1]
print(ma)