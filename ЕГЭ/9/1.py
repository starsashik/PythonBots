c=0
with open("9 (1).txt") as f:
    d = f.readlines()
    for i in d:
        s = list(map(int, i.split()))
        if len(set(s)) == 5:
            ch = sum(s) - sum(set(s))
            s.remove(ch)
            s.remove(ch)
            if ch*2 >= sum(s) / len(s):
                c += 1
print(c)